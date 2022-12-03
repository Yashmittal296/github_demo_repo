import pandas as pd

dict_data = [
    {
        "country": "China",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": True,
        "vpnRestricted": True
    },
    {
        "country": "Indonesia",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Pakistan",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Bangladesh",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Vietnam",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Iran",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": True,
        "vpnRestricted": True
    },
    {
        "country": "Turkey",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Thailand",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Tanzania",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "South Korea",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Uganda",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Afghanistan",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Saudi Arabia",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Uzbekistan",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Malaysia",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Yemen",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Nepal",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "North Korea",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": True,
        "vpnRestricted": True
    },
    {
        "country": "Syria",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Cambodia",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Belarus",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": True,
        "vpnRestricted": True
    },
    {
        "country": "United Arab Emirates",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Laos",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Turkmenistan",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Oman",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Kuwait",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Eritrea",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Armenia",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Qatar",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Equatorial Guinea",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Bahrain",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Maldives",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Brunei",
        "pornBanned": True,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "India",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "United States",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Nigeria",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Brazil",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Russia",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Mexico",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Japan",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Ethiopia",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Philippines",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Egypt",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Germany",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "United Kingdom",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "France",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "South Africa",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Italy",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Kenya",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Colombia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Spain",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Sudan",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Argentina",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Algeria",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Iraq",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": True,
        "vpnRestricted": True
    },
    {
        "country": "Poland",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Ukraine",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Canada",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Morocco",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Angola",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Peru",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Mozambique",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Madagascar",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Venezuela",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Cameroon",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Niger",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Australia",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Taiwan",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Burkina Faso",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Mali",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Sri Lanka",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Malawi",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Zambia",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Romania",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Chile",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Kazakhstan",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Ecuador",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Guatemala",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Chad",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Somalia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Netherlands",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Senegal",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Zimbabwe",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Guinea",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Rwanda",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Benin",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Burundi",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Tunisia",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Bolivia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Belgium",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Jordan",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Cuba",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "South Sudan",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Sweden",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Czech Republic",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Honduras",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Greece",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Azerbaijan",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Portugal",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Papua New Guinea",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Hungary",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Tajikistan",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": True
    },
    {
        "country": "Israel",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Austria",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Togo",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Switzerland",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Sierra Leone",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Hong Kong",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Serbia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Nicaragua",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Libya",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Bulgaria",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Paraguay",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Kyrgyzstan",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "El Salvador",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Singapore",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Denmark",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Slovakia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Central African Republic",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Finland",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Lebanon",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Norway",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Liberia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Palestine",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "New Zealand",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Costa Rica",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Ireland",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Mauritania",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Panama",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Croatia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Georgia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Uruguay",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Mongolia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Moldova",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Bosnia and Herzegovina",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Albania",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Lithuania",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Gambia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Botswana",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Namibia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Gabon",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Lesotho",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Slovenia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Guinea-Bissau",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Latvia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Trinidad and Tobago",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Timor-Leste",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Estonia",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Mauritius",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Cyprus",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Eswatini",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Djibouti",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Fiji",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Comoros",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Guyana",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Bhutan",
        "pornBanned": False,
        "pornRestricted": True,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Luxembourg",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Montenegro",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Suriname",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Cape Verde",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Malta",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Belize",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Iceland",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Samoa",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Seychelles",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Tonga",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Andorra",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    },
    {
        "country": "Liechtenstein",
        "pornBanned": False,
        "pornRestricted": False,
        "vpnBanned": False,
        "vpnRestricted": False
    }
]

data = pd.DataFrame(dict_data)

country = str(input())
rslt_df = data[data['country'] == country]
print(rslt_df)
