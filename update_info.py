# TODO Maybe communication via JSON file which would also help data analysis 
def update_info(country, genre, markdown_file='current_week.md'):
    """Adding info to README about what i'm listening this week

    Args:
        country (string): Which country
        genre (string): what
        markdown_file (str, optional): save. Defaults to 'current_week.md'.
    """
    with open('current_week.md', 'r') as f:
        info = f'{genre}'
        # f.write()