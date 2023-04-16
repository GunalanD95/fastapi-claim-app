# <ins> CLAIM PROCESS - FASTAPI </ins>

### TASK REQUIREMENTS
1. **claim_process** transforms a JSON payload representing a single claim input with multiple lines and stores it into a RDB.
   - An example input (in CSV format) - *claim_1234.csv* is provided. Note that the names are not consistent in capitalization.
2. **claim_process** generates a unique id per claim.
3. **claim_process** computes the *“net fee”* as a result per the formula below.
*“net fee” = “provider fees” + “member coinsurance” + “member copay” - “Allowed fees”* (note again that the names are not consistent in capitalization).
4. A downstream service, **payments**, will consume *“net fee”* computed by **claim_process**.



### APPROACH FOR DOWNSTREAM PAYMENTS COMMUNICATION:
``` 
  Points to be considered :
   - What needs to be done if there is a failure in either service and steps need to be unwinded.
   - Multiple instances of either service are running concurrently to handle a large volume of claims.

  1. Using Queue can be good approach i think .
  2. When the claim process happens , we will send everything to Some Queue .
  3. Then Payments downstream service will take the data (net_fee) computed by claim process
  4. by this way we can avoid downtime of anyservice too , the queue will handle .
  5. this approach will make sure resilient to failures.
  6. since fastapi is async already , it handles requests concurrently
```


### BUILD AND RUN USING DOCKER IMAGE

- Build Docker Image
```
  docker build -t my-fastapi-app .

```

- Run the image
```
  docker run -d -p 8000:8000 my-new-app
```

- enter into the pod
```
  docker exec -it pod-name bash
```

### INSTRUCTIONS :
- CREATE   VIRTUAL ENVIRONMENT 
```
   py -3 -m venv env

```
- ACTIVATE VIRTUTAL ENVIRONMENT
```
 source env/Scripts/activate
```

- INSTALL REQUIREMENT.txt
```
  pip3 install requirments.txt
```

- RUN THE APP [outside the app folder]
```
uvicorn fast_api_app.main:app --host 0.0.0.0 --port 8000

```


## ROUTES 
| Endpoint      | Functionality  | Request Method | 
| ------------- | -------------- | -------------- |
| /claim        | Submit a claim | POST           |

#### EXAMPLE INPUT :
```
{
  "claims": [
    {
      "service_date": "3/28/18 0:00",
      "submitted_procedure": "D0180",
      "quadrant": null,
      "plan_group": "GRP-1000",
      "subscriber": "3730189502",
      "provider_npi": "1497775530",
      "provider_fees": 100.0,
      "allowed_fees": 100.0,
      "member_coinsurance": 0.0,
      "member_copay": 0.0
    },
    {
      "service_date": "3/28/18 0:00",
      "submitted_procedure": "D0210",
      "quadrant": null,
      "plan_group": "GRP-1000",
      "subscriber": "3730189502",
      "provider_npi": "1497775530",
      "provider_fees": 108.0,
      "allowed_fees": 108.0,
      "member_coinsurance": 0.0,
      "member_copay": 0.0
    },
    {
      "service_date": "3/28/18 0:00",
      "submitted_procedure": "D4346",
      "quadrant": null,
      "plan_group": "GRP-1000",
      "subscriber": "3730189502",
      "provider_npi": "1497775530",
      "provider_fees": 130.0,
      "allowed_fees": 65.0,
      "member_coinsurance": 16.25,
      "member_copay": 0.0
    },
    {
      "service_date": "3/28/18 0:00",
      "submitted_procedure": "D4211",
      "quadrant": "UR",
      "plan_group": "GRP-1000",
      "subscriber": "3730189502",
      "provider_npi": "1497775530",
      "provider_fees": 178.0,
      "allowed_fees": 178.0,
      "member_coinsurance": 35.6,
      "member_copay": 0.0
    }
  ]
}


```


### RUN TESTS [run inside the folder]
```
py -3 tests.py
```


### ULTIIZED RESOURCES 

- TESTING -> https://fastapi.tiangolo.com/tutorial/testing/

- DOCKER  -> https://docs.docker.com/compose/compose-file/
