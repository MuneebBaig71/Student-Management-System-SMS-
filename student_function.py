def main(students_data):
    for students in students_data:
        print(f"my name is {students['name']} and my marks are {students['marks']} and my total marks are {sum(students['marks'].values())}")

students_data = [
    {
        'name': 'John Doe',
        'marks': {
            'Math': 85,
            'English': 90,
            'Science': 78
        }
    },
    {
        'name': 'Jane Smith',
        'marks': {
            'Math': 75,
            'English': 82,
            'Science': 89
        }
    },
    {
        'name': 'Emily Davis',
        'marks': {
            'Math': 93,
            'English': 87,
            'Science': 85
        }
    },
    {
        'name': 'Michael Brown',
        'marks': {
            'Math': 65,
            'English': 70,
            'Science': 60
        }
    },
    {
        'name': 'Chris Johnson',
        'marks': {
            'Math': 88,
            'English': 85,
            'Science': 90
        }
    }
]


main(students_data)