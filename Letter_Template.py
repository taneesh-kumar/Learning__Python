letter = '''Dear <|Name|>
            you are selected!
            <|Date|>'''

print(letter.replace('<|Name|>', 'Taneesh').replace('<|Date|>', '26/11/24'))