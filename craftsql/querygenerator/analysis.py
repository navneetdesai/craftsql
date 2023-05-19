from .models import UserActivity
import pandas as pd
import matplotlib.pyplot as plt

def generate_report():

    user_activities = UserActivity.objects.all()

    df = pd.DataFrame(list(user_activities.values('functionality', 'timestamp')))

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df['hour'] = df['timestamp'].dt.hour

    functionality_counts = df['functionality'].value_counts()

    plt.figure(figsize=(8, 6))
    functionality_counts.plot(kind='bar')
    plt.xlabel('Functionality')
    plt.ylabel('Usage Count')
    plt.title('Functionality Usage')
    plt.xticks(rotation=45)
    plt.show()

    hourly_counts = df['hour'].value_counts().sort_index()

    plt.figure(figsize=(8, 6))
    hourly_counts.plot(kind='line', marker='o')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Traffic Count')
    plt.title('Traffic by Hour of the Day')
    plt.xticks(range(24))
    plt.grid(True)
    plt.show()
