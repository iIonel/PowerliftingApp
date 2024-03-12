
## API Reference

#### Get all users

```http
  GET /users/
```
#### Get all users by id

```http
  GET /users/${id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | **Required** |

#### Get all users by status 💉

```http
  GET /users/status/${natty}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `natty` | `bool` | **Required** |

#### Get user by email

```http
  GET /users/email/${email}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required** |

#### Get all exercises

```http
  GET /exercises/
```

#### Post user

```http
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

```http
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

```http
  POST /exercises/add/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `exercise_id`      | `int` | Auto Increment  **NO Required**|
| `name`      | `string` | **Required** |
| `description`   | `string`|  **Required**|          
| `video_link`   | `string`|  **Required**| 

#### Delete user
```http
  DELETE /users/delete/
```

#### Delete exercise

```http
  DELETE /exercises/delete/
```

#### Put user

```http
  PUT /users/update/
```

#### Put exercise

```http
  PUT /exercises/update/
```




