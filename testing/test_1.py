from time import time
from requests import get, post
from multiprocessing.pool import ThreadPool
LONG_TEXT = """Quota politics is back in play to favour, this time, students from 
government higher secondary schools in Tamil Nadu. The Cabinet’s nod on Monday, 
for an ordinance to create a horizontal 7.5% reservation of the State’s 
quota of seats in medical colleges, is a well-intentioned move to address 
the problem of poor representation from government schools in MBBS/BDS courses 
which has been in existence even prior to the introduction of NEET for admission. 
The issue of inequity has come in for criticism against NEET which came into 
operation in Tamil Nadu in 2017. Since then, there has been a high-decibel campaign, 
against NEET and the AIADMK government, led by Edappadi K. Palaniswami, on the ground 
that the design and form of the test are loaded against students of rural areas, 
government schools, Backward and Most Backward Classes, and Scheduled Castes/Scheduled Tribes. 
Like in the case of other professional course entrance tests, most candidates clearing 
NEET in Tamil Nadu are invariably those who undergo private coaching. 
It was also in the last three years that the AIADMK regime veered closer towards 
the BJP-led government at the Centre. Despite the authorities asserting that NEET is neither 
against communal reservation nor weaker sections, the campaign appears to have had an 
impact during the 2019 Lok Sabha polls as the DMK-led front won 38 out of 39 seats. 
The State’s latest decision comes in the backdrop of this factor and also of next year’s Assembly election."""

max_length = 30


def make_request(text):
    # r = get('http://127.0.0.1:5000/').json()
    r = post('http://127.0.0.1:5000/summary', data={'text': text, 'max_length': max_length})

    return (r.json(), r.status_code)


def async_request(n_request):
    pool = ThreadPool()
    result = pool.map_async(
        make_request, [LONG_TEXT for _ in range(n_request)]
    )
    pool.close()

    return result.get()


if __name__ == '__main__':

    start_time = time()

    N_REQUEST = 2
    result = async_request(n_request=N_REQUEST)

    print(result)
    print(f'Required time for {N_REQUEST} requests: {time() - start_time:.2f}')
