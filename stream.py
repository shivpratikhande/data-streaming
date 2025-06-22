from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
import uuid

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 10,00),
    
}

def get_data():
    import requests
    
    res = requests.get('https://randomuser.me/api/', stream=True)
    res = res.json()
    res = res['results'][0]
    return res


def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():
    import json
    
    res = get_data()
    res = format_data(res)
    res= json.dumps(res, indent=3)
    print(res)
    
    
stream_data()
# with DAG('user automation',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:
    
#     streaming_task = PythonOperator(
#         task_id='streaming_task',
#         python_callable=stream_data,
#         dag=dag     
    
# )
    