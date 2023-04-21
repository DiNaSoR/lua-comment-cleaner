# Copyright (C) 2023 DiNaSoR
# This program is free software; you can redistribute it and/or modify
# it under the terms of the MIT License.

import re

def remove_comments_from_lua(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    cleaned_content = []
    inside_multiline_comment = False
    comment_level = -1

    for line in content.splitlines(True):
        cleaned_line = line

        if not inside_multiline_comment:
            # Removing single line comments
            if '--' in line:
                cleaned_line = line.split('--', 1)[0] + '\n'

            # Removing multi-line comments
            multiline_comment_start = re.search(r'--\[(=*)\[', line)
            if multiline_comment_start:
                cleaned_line = line.split(multiline_comment_start.group(0), 1)[0]
                inside_multiline_comment = True
                comment_level = len(multiline_comment_start.group(1))

        if inside_multiline_comment:
            multiline_comment_end = re.search(r']=(=*)]', line)
            if multiline_comment_end and len(multiline_comment_end.group(1)) == comment_level:
                cleaned_line = cleaned_line.split(multiline_comment_end.group(0), 1)[1]
                inside_multiline_comment = False
                comment_level = -1

        cleaned_content.append(cleaned_line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_content)

# Usage example:
remove_comments_from_lua('Input.LUA', 'Output.LUA')
