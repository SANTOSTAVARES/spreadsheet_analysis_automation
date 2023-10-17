import win32com.client


def send_email(sheet_identification: str,
               sheet_information: dict,
               rule_description: str,
               main_column: str,
               row_value_outside_rule: str,
               recipients_emails: list) -> None:

    recipients_emails_as_str = ""
    for email in recipients_emails:
        recipients_emails_as_str += email + "; "

    ol = win32com.client.Dispatch('Outlook.Application')
    olmailitem = 0x0
    newmail = ol.CreateItem(olmailitem)
    newmail.Subject = 'Validação automática de dados da Smartsheet'
    newmail.To = recipients_emails_as_str

    newmail.HTMLbody = (
        f""" <!DOCTYPE html>
        <html lang="pt-br">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Formatação de Textos</title>
        </head>

        <style>
            table, th, td {{
            border:1px solid black;
            }}
        </style>
        
        <body>
            <p>Este é um e-mail automático, gerado por ter sido encontrado divergências em relação a regra para coluna e planilha descrita abaixo.</p>
            <p><b>ID:</b> {sheet_identification}</p>
            <p><b>Planilha:</b> {sheet_information["name"]}</p>
            <p><b>Coluna:</b> {main_column}</p>
            <p><b>Link:</b> {sheet_information["permalink"]}</p>
            <p><b>Regra de validação:</b> {rule_description}</p>

            <table>
                <tr>
                    <th>Linha</th>
                    <th>Valor</th>
                </tr>
                {row_value_outside_rule}         
            </table>
        </body>
        </html> 
    """
    )
    newmail.Send()
    return None
