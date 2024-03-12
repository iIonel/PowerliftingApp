
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




