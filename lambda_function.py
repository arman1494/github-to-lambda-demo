
import pandas as pd

def lambda_handler(event, context):
    """_summary_

    Args:
        event (_type_): _description_
        context (_type_): _description_
    """
    data = {'col1':[1,2], 'col2':[3,4]}
    df = pd.DataFrame(data=data)
    print(df)
    print('Done!')