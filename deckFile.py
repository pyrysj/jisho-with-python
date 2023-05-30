import pandas as pd

# became less complicated than anticipated
def convertToImportForm(df: pd.DataFrame):
    new_df = df
    # These could really be merged but i feel that a step by step approach is better here
    # first: merge the definitions into one string
    new_df[5] = new_df[5].apply(lambda x:['; '.join(l) for l in x])
    # second: enumerate said strings and then add some stuff to allow for new row in the card.
    # NB: use <br> for anki! see: https://docs.ankiweb.net/importing.html
    new_df[5] = new_df[5].apply(lambda x:[f"{i+1}. {defs}<br>" for i, defs in enumerate(x)])
    # third: convert fully to string
    new_df[5] = new_df[5].apply(lambda x: ''.join(x))
    return new_df