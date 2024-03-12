
## API Reference

#### Get all users

```
  GET /users/
```
#### Get all users by id

```
  GET /users/${id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required** |

#### Get all users by status 💉

```
  GET /users/status/${natty}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `natty` | `bool` | **Required** |

#### Get user by email

```
  GET /users/email/${email}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required** |

#### Get all exercises

```
  GET /exercises/
```

#### Post user

```
  POST /users/add/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_id`      | `int` | Auto Increment  **NO Required**|
| `first_name`   | `string`|  **Required**|          
| `last_name`   | `string`|  **Required**| 
| `email`   | `string`|  **Required**|    
| `age`   | `int`|  **Required**|
| `weight`   | `float`|  **Required**|  
| `height`   | `float`|  **Required**|  

#### Post personal record

```
  POST /users/add_record/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `pr_id`      | `int` | Auto Increment  **NO Required**|
| `user_id`      | `int` | **Required** REFERENCES users|
| `squat`   | `int`|  **Required**|          
| `bench`   | `int`|  **Required**| 
| `deadlift`   | `int`|  **Required**|    

#### Post exercise

```
  POST /exercises/add/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `exercise_id`      | `int` | Auto Increment  **NO Required**|
| `name`      | `string` | **Required** |
| `description`   | `string`|  **Required**|          
| `video_link`   | `string`|  **Required**| 

#### Delete user
```
  DELETE /users/delete/
```

#### Delete exercise

```
  DELETE /exercises/delete/
```

#### Put user

```
  PUT /users/update/
```

#### Put exercise

```
  PUT /exercises/update/
```


## Database 


```bash
 CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    age INT,
    natty BOOLEAN,
    weight FLOAT,
    height FLOAT,
);

CREATE TABLE personalrecords (
    pr_id SERIAL PRIMARY KEY,
    squat FLOAT,
    bench FLOAT,
    deadlift FLOAT,
    user_id INT REFERENCES users(user_id),
);

CREATE TABLE programs (
    program_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    user_id INT REFERENCES users(user_id),
);

CREATE TABLE workouts (
    workout_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    program_id INT REFERENCES programs(program_id),
    week_number INT,
    day_number INT
);

CREATE TABLE exercises (
    exercise_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    video_link VARCHAR(200)
);

CREATE TABLE workout_items (
    item_id SERIAL PRIMARY KEY,
    exercise_id INT REFERENCES exercises(exercise_id),
    workout_id INT REFERENCES workouts(workout_id)
);

CREATE TABLE sets (
    set_id SERIAL PRIMARY KEY,
    rep_count INT,
    workout_item_id INT REFERENCES workout_items(item_id),
    weight FLOAT
);


```




