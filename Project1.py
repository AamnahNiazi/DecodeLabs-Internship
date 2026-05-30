my_tasks = []
my_tasks.append('MUST DO THIS')
my_tasks.append('YOU MUST DO THIS')
my_tasks.append('OK FINE DO THIS')
enumerate(my_tasks)
(0, 'MUST DO THIS')
(1, 'YOU MUST DO THIS')
(2, 'OK FINE DO THIS')
{
    "id": 1,
    "task": "MUST DO THIS"
}
{
    "id": 2,
    "task": "YOU MUST DO THIS"
}
{
    "id": 3,
    "task": "OK FINE DO THIS"
}

def main():
    for index, task in enumerate(my_tasks):
        print({
            "id": index + 1,
            "task": task
        })

if __name__ == "__main__":
   main()
