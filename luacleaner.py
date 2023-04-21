# Copyright (C) 2023 DiNaSoR
# This program is free software; you can redistribute it and/or modify
# it under the terms of the MIT License.

def remove_comments_from_lua(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    cleaned_content = []
    inside_multiline_comment = False
    for line in content.splitlines(True):
        cleaned_line = line

        if not inside_multiline_comment:
            # Removing single line comments
            if '--' in line:
                cleaned_line = line.split('--', 1)[0] + '\n'

            # Removing multi-line comments
            if '--[[' in line:
                cleaned_line = line.split('--[[', 1)[0]
                inside_multiline_comment = True

        if inside_multiline_comment:
            if ']]' in line:
                cleaned_line = cleaned_line.split(']]', 1)[1]
                inside_multiline_comment = False

        cleaned_content.append(cleaned_line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_content)

# Usage example:
remove_comments_from_lua('Input.LUA', 'Output.LUA')