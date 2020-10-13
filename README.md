# Instructions

- Build this docker image, use it as your base (read more [here](https://github.com/puckel/docker-airflow))
- You can run `bash` as the command with an interactive tty to get into the image:

```
docker run --rm -it ${whatever-you-named-the-image} /bin/bash
```

- Setup a local database within the docker image. The only restriction here is that you cannot use Airflow's database

- Write an Airflow DAG that will:

  1. Download the first 100 datasets from https://github.com/datasets
  2. Load the data into the database that you setup.
  3. Answer the questions [below](README.md#Questions) and output it to a table in your database in this format:

  ```
  |Question|Answer|
  |--------|------|
  | 1      | 1000 |
  ```

  4. Ensure that we can `docker run` and then use `localhost:$PORT` to see the solution running.

- Lastly, create a Pull Request with your code for review

# Questions

## what's the average number of fields across all the `.csv` files?

output should be a simple number

_sample output_

```
5
```

## create a csv file that shows the word count of every value of every dataset (dataset being a `.csv` file)

output should be a csv file that has a header row with fields `value` and
`count` and one entry for every value found:

_sample output_

```
value,count
some value,435
another value,234
word,45
...
```

## what's the total number or rows for the all the `.csv` files?

output should be a simple number

_sample output_

```
1000000000
```
