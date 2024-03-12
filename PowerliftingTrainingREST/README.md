
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
    id_user INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
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

