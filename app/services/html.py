def list_of_row_value_outside_rule_converted_to_html_table_lines(row_value_outside_rule: list) -> str:
    table_lines = ""
    for i in row_value_outside_rule:

        list_converted_to_html_table_lines = f"""<tr>
            <td>{i[0]}</td>
            <td>{i[1]}</td>
        </tr>"""

        table_lines += list_converted_to_html_table_lines

    return table_lines
