RAJASTHAN_CITIES = [
    "Jaipur", "Jodhpur", "Udaipur", "Bikaner", "Ajmer", "Pushkar", "Kota",
    "Alwar", "Bharatpur", "Jaisalmer", "Bundi", "Chittaurgarh", "Chittorgarh",
    "Mount Abu", "Sawai Madhopur", "Ranthambore National Park", "Ranakpur",
    "Kumbhalgarh", "Nathdwara", "Kishangarh", "Sikar", "Pali", "Barmer", "Jalore",
    "Nagaur", "Jhalawar", "Tonk", "Baran", "Dungarpur", "Banswara", "Churu",
    "Hanumangarh", "Sri Ganganagar", "Dausa", "Karauli", "Dholpur", "Sirohi",
    "Jhunjhunu", "Mandawa", "Nawalgarh", "Shekhawati", "Osian", "Pokaran",
    "Pokhran", "Deeg"
]

def filter_rajasthan(df):
    return df[df["City"].isin(RAJASTHAN_CITIES)].copy()
