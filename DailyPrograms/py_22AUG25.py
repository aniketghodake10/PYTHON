"""
Parse the logs into a structured format (dictionary or namedtuple) with fields:
timestamp (as Python datetime)
user_id
url
status_code (as int)

Compute:

✅ Total requests per user

✅ Most visited URL

✅ Count of failed requests (status_code >= 400) per user

✅ User who visited the site the most within any 5-minute window

Return results in a clean dictionary format.

Expected output -
{
    "requests_per_user": {"user1": 3, "user2": 2, "user3": 1},
    "most_visited_url": "/home",
    "failed_requests": {"user1": 1, "user3": 1},
    "top_user_in_5min": "user1"
}
"""

from datetime import datetime as dt
import pandas as pd

logs = [
    "[2025-08-20 10:15:32] user1 /home 200",
    "[2025-08-20 10:16:10] user2 /products 200",
    "[2025-08-20 10:16:45] user1 /cart 500",
    "[2025-08-20 10:17:01] user3 /home 404",
    "[2025-08-20 10:18:12] user2 /checkout 200",
    "[2025-08-20 10:20:55] user1 /home 200",
]

parsed_logs = []
log_dict = {}
for log in logs:
    ilog = []
    ilog.append(dt.strptime(log[1:20], "%Y-%m-%d %H:%M:%S"))
    ilog = ilog + log[22:].split(" ")
    parsed_logs.append(ilog)
print(parsed_logs)

df = pd.DataFrame(parsed_logs, columns=["datetime", "userid", "url", "status"])
print(df)

df_requests_per_user = df.groupby("userid").agg(user_count=('userid', 'count'))
print(df_requests_per_user)

df_url = df.groupby("url").agg(url_count=('url', 'count'))
print(df_url[df_url["url_count"]==df_url["url_count"].max()])

df_failed_requests_per_user = df[df["status"]!="200"].groupby("userid").agg(user_count=('userid', 'count'))
print(df_failed_requests_per_user)
