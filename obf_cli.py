#!/usr/bin/env python3
"""
ObfuXtreme selective wrapper (NO string encryption).

Default behavior:
 - Writes the transformed, human-readable Python source (renamed + CFF) to -o

If you want the encrypted loader instead, pass --loader.

Usage examples:
  # default: write readable transformed source
  python obf_cli.py -i matmul.py -o L1/Obf_matmul.py --var-rename --control-flow-flattening --map-output L1/map.json

  # write encrypted loader instead (old behavior)
  python obf_cli.py -i matmul.py -o L1/Obf_matmul_loader.py --var-rename --control-flow-flattening --loader
"""

import argparse
import importlib
import os
import sys
import ast
import marshal
import zlib
import base64
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def import_obfuscator():
    try:
        mod = importlib.import_module("ObfuXtreme.ObfuXtreme")
        return mod.UltimateObfuscator
    except Exception as e:
        print(f"[ERROR] Could not import ObfuXtreme.ObfuXtreme: {e}", file=sys.stderr)
        sys.exit(1)

def read_source(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def apply_transforms_and_get_artifacts(obf_cls, source_code, use_var_rename, use_cff):
    """
    Returns tuple: (marshalled_bytes, transformed_ast, renamer_map_or_None)
    """
    tree = ast.parse(source_code)

    renamer_map = None
    # collect assigned vars & run renamer if requested
    if use_var_rename:
        if not hasattr(obf_cls, "VariableCollector"):
            raise RuntimeError("Original class missing VariableCollector.")
        collector = obf_cls.VariableCollector()
        collector.visit(tree)
        assigned_vars = getattr(collector, "assigned_vars", set())

        if not hasattr(obf_cls, "VariableRenamer"):
            raise RuntimeError("Original class missing VariableRenamer.")
        renamer = obf_cls.VariableRenamer(assigned_vars)
        tree = renamer.visit(tree)
        ast.fix_missing_locations(tree)
        renamer_map = getattr(renamer, "var_map", None)

    # apply CFF if requested
    if use_cff:
        if not hasattr(obf_cls, "ControlFlowFlattener"):
            raise RuntimeError("Original class missing ControlFlowFlattener.")
        cff = obf_cls.ControlFlowFlattener()
        tree = cff.visit(tree)
        ast.fix_missing_locations(tree)

    compiled = compile(tree, "<obfuscated>", "exec")
    marshalled = marshal.dumps(compiled)
    return marshalled, tree, renamer_map

def ast_to_source(tree):
    """
    Convert AST to readable source. Prefer ast.unparse(), fallback to astor.
    """
    if hasattr(ast, "unparse"):
        return ast.unparse(tree)
    try:
        import astor
        return astor.to_source(tree)
    except Exception as e:
        raise RuntimeError("No AST-to-source available. Install Python 3.9+ or pip install astor") from e

def build_loader_from_instance_and_marshalled(instance, marshalled_bytes):
    compressed = zlib.compress(marshalled_bytes, level=9)
    if not (hasattr(instance, "aes_key") and hasattr(instance, "iv")):
        raise RuntimeError("Original instance missing aes_key/iv attributes.")
    cipher = AES.new(instance.aes_key, AES.MODE_CBC, instance.iv)
    encrypted = cipher.encrypt(pad(compressed, 16))
    encrypted_b85 = base64.b85encode(encrypted).decode()
    # prefer original _build_loader if available
    if hasattr(instance, "_build_loader") and callable(getattr(instance, "_build_loader")):
        return instance._build_loader(encrypted_b85)
    # fallback loader
    return f'''# Loader fallback
import sys, os, base64, marshal, zlib, traceback
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

_KEY = {instance.aes_key!r}
_IV  = {instance.iv!r}

def _decrypt_str(data):
    try:
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        return unpad(cipher.decrypt(data), 16).decode()
    except:
        return ""

def _main():
    try:
        _encrypted = {encrypted_b85!r}
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        encrypted_data = base64.b85decode(_encrypted)
        decrypted = cipher.decrypt(encrypted_data)
        try:
            decrypted = unpad(decrypted, 16)
        except:
            pass
        decompressed = zlib.decompress(decrypted)
        exec(marshal.loads(decompressed), {{**globals(), '__name__':'__main__', '_decrypt_str':_decrypt_str}})
    except Exception:
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    _main()
'''

def main(argv=None):
    parser = argparse.ArgumentParser(description="ObfuXtreme selective wrapper (default: write transformed source).")
    parser.add_argument("-i", "--input", required=True, help="Input Python file")
    parser.add_argument("-o", "--output", required=True, help="Output path (default: transformed source).")
    parser.add_argument("--var-rename", action="store_true", help="Apply Variable Renaming")
    parser.add_argument("--control-flow-flattening", action="store_true", help="Apply Control Flow Flattening")
    parser.add_argument("--loader", action="store_true", help="Write encrypted loader instead of readable transformed source")
    args = parser.parse_args(argv)

    if not os.path.isfile(args.input):
        print(f"[ERROR] Input file not found: {args.input}", file=sys.stderr)
        sys.exit(2)
    if not (args.var_rename or args.control_flow_flattening):
        print("[ERROR] No transform selected. Use --var-rename and/or --control-flow-flattening.", file=sys.stderr)
        sys.exit(3)

    UltimateObfuscator = import_obfuscator()

    # instantiate original class (it expects filename)
    try:
        obf_inst = UltimateObfuscator(args.input)
    except TypeError:
        obf_inst = UltimateObfuscator()
        if hasattr(obf_inst, "filename"):
            setattr(obf_inst, "filename", args.input)
    # ensure instance.code is the latest source
    source = read_source(args.input)
    obf_inst.code = source

    # perform transforms
    try:
        marshalled, transformed_ast, renamer_map = apply_transforms_and_get_artifacts(
            obf_cls=UltimateObfuscator,
            source_code=source,
            use_var_rename=args.var_rename,
            use_cff=args.control_flow_flattening
        )
    except Exception as e:
        print(f"[ERROR] AST transformation failed: {e}", file=sys.stderr)
        raise

    # default action: write the readable transformed source to args.output
    # If --loader is provided, write encrypted loader instead.
    if not args.loader:
        # convert AST -> source and write
        try:
            pretty_src = ast_to_source(transformed_ast)
        except Exception as e:
            print(f"[ERROR] Converting AST to source failed: {e}", file=sys.stderr)
            raise
        os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as df:
            df.write(pretty_src)
        print(f"[SUCCESS] Wrote transformed readable source to: {args.output}")
    else:
        # build encrypted loader and write to -o
        try:
            loader_src = build_loader_from_instance_and_marshalled(obf_inst, marshalled)
            os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
            with open(args.output, "w", encoding="utf-8") as of:
                of.write(loader_src)
            print(f"[SUCCESS] Wrote encrypted loader to: {args.output}")
        except Exception as e:
            print(f"[ERROR] Failed to build/write loader: {e}", file=sys.stderr)
            raise

    # print AES key info for debugging (loader path only)
    try:
        print(f"[INFO] AES key (hex): {obf_inst.aes_key.hex()}")
    except Exception:
        pass

if __name__ == "__main__":
    main()
