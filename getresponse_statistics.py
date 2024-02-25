## testowy pobranie listy subskrybentów
import requests
import pandas as pd

def get_campaigns_stats(api_key):
    url = "https://api.getresponse.com/v3/campaigns/statistics/list-size"
    headers = {"X-Auth-Token": f"api-key {api_key}"}
    params = {
        "query[campaignId]": "YOUR-CAMPAIGN-ID" #ENTER YOUR CAMPAIGN ID HERE
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # CHECK FOR CODE 2xx (SUCCESS)
        campaigns_stats_data = response.json()
        return campaigns_stats_data
    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas żądania API:", e)
        return None

if __name__ == "__main__":
    api_key = "API_KEY_TEST" # Enter your API here
    campaigns_stats = get_campaigns_stats(api_key)
    if campaigns_stats:
        print("Pobrane dane:")
        print(campaigns_stats)
        df = pd.DataFrame(campaigns_stats)
		
		
import requests
import pandas as pd

def get_newsletters(api_key):
    url = "https://api.getresponse.com/v3/newsletters"
    headers = {"X-Auth-Token": f"api-key {api_key}"}
    params = {
        "perPage": "100000"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # CHECK FOR CODE 2xx (SUCCESS)
        newsletters_data = response.json()
        return newsletters_data
    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas żądania API:", e)
        return None

if __name__ == "__main__":
    api_key = "API_KEY_TEST" # Enter your API here
    newsletters = get_newsletters(api_key)
    if newsletters:
        print("Pobrane dane:")
        print(newsletters)
        df = pd.DataFrame(newsletters)

        # Konwertujemy kolumnę "sendOn" na typ daty
        df["sendOn"] = pd.to_datetime(df["sendOn"])

        # Sortujemy DataFrame rosnąco po kolumnie "sendOn"
        df_sorted = df.sort_values(by="sendOn", ascending=True)

        # Wyodrębniamy dane JSON ze struktur kolumn "campaign", "sendSettings" i "sendMetrics"
        df_campaign = pd.json_normalize(df_sorted["campaign"])
        df_send_settings = pd.json_normalize(df_sorted["sendSettings"])
        df_send_metrics = pd.json_normalize(df_sorted["sendMetrics"])

        # Łączymy wyodrębnione dane z powrotem z DataFrame "df_sorted"
        df_sorted = pd.concat([df_sorted, df_campaign, df_send_settings, df_send_metrics], axis=1)
        df_sorted_final = df_sorted

        # Nazwy kolumn w DataFrame
        print(df_sorted.columns)

        print("\nDane zapisane do DataFrame (posortowane rosnąco po sendOn, z wyodrębnionymi danymi JSON):")
        print(df_sorted_final)


# Wybierz kolumnę "campaignId" i użyj metody drop_duplicates() do utworzenia nowego DataFrame z unikalnymi wartościami
distinct_campaignIds_df = df_sorted[['campaignId']].drop_duplicates()

print(distinct_campaignIds_df)

#Tworzenie tabeli
table_data_list_campaignIds = list(distinct_campaignIds_df['campaignId'])

# Wyświetlenie tabeli
print(table_data_list_campaignIds)


# Wybierz kolumnę "newsletterId" i użyj metody drop_duplicates() do utworzenia nowego DataFrame z unikalnymi wartościami
distinct_newsletterIds_df = df_sorted[['newsletterId']].drop_duplicates()

print(distinct_newsletterIds_df)
table_data_list_newsletterIds = list(distinct_newsletterIds_df['newsletterId'])

# Wyświetlenie tabeli
print(table_data_list_newsletterIds)

print(table_data_list_newsletterIds)
print(table_data_list_campaignIds)

import requests
import pandas as pd

def get_newsletters_statistics(api_key, newsletter_id, campaign_id):
    url = "https://api3.getresponse360.pl/v3/newsletters/statistics"
    headers = {"X-Auth-Token": f"api-key {api_key}"}

    params = {
        "query[newsletterId]": newsletter_id,
        "query[campaignId]": campaign_id,
        "groupBy": "day",
        "perPage": "100000"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        newsletters_data = response.json()
        return newsletters_data
    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas żądania API:", e)
        return None

if __name__ == "__main__":
    api_key = "API_KEY_TEST" # Enter your API here    
	table_data_list_newsletterIds = list(distinct_newsletterIds_df['newsletterId'])  # Lista z identyfikatorami newsletterów
    table_data_list_campaignIds = list(distinct_campaignIds_df['campaignId'])  # Lista z identyfikatorami kampanii

    # Inicjalizujemy pustą listę, która będzie przechowywać wyniki
    results_list = []

    for newsletter_id in table_data_list_newsletterIds:
        for campaign_id in table_data_list_campaignIds:
            results = get_newsletters_statistics(api_key, newsletter_id, campaign_id)
            if results:
                # Add newsletterId and campaignId to each result dictionary
                for result in results:
                    result['newsletterId'] = newsletter_id
                    result['campaignId'] = campaign_id
                results_list.extend(results)

    if results_list:
        print("Pobrane dane:")
        print(results_list)
        # Tworzymy DataFrame z połączonych wyników
        df = pd.DataFrame(results_list)
        print(df)

import requests
import pandas as pd

# Define your distinct_campaignIds_df DataFrame here

def get_campaigns_stats(api_key, campaign_id):
    url = "https://api.getresponse.com/v3/campaigns/statistics/list-size"
    headers = {"X-Auth-Token": f"api-key {api_key}"}
    params = {
        "query[campaignId]": campaign_id,
        "groupBy": "day",
        "perPage": "100000"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Check if the response returns a 2xx status code
        campaigns_stats_data = response.json()
        return campaigns_stats_data
    except requests.exceptions.RequestException as e:
        print("Error while making the API request:", e)
        return None

if __name__ == "__main__":
    api_key = "API_KEY_TEST" # Enter your API here
    table_data_list_campaignIds = list(distinct_campaignIds_df['campaignId'])

    # Initialize an empty list to store results
    results_list = []

    for campaign_id in table_data_list_campaignIds:
        results = get_campaigns_stats(api_key, campaign_id)
        if results:
            for result in results:
                result['campaignId'] = campaign_id  # Assign campaign_id to each result
            results_list.extend(results)

    if results_list:
        print("Fetched data:")
        print(results_list)
        # Create a DataFrame from the combined results
        df = pd.DataFrame(results_list)
        print(df)
