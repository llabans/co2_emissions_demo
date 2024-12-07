# Query for 5 countries (adjust these to any countries you like)
countries_of_interest = ["Namibia", "Peru", "Kenya", "Uganda", "Nigeria"]
for country in countries_of_interest:
    country_data = emissions_long_1990_2022.query("country == @country")
    fig = px.line(
        country_data, x="year", y="emissions", title=f"Emissions for {country}"
    )
    fig.show()

# Create a line chart with all selected countries
# Year should be on the x-axis, emissions on the y-axis,
# and color should be by country.
fig_chart = px.line(
    emissions_long_1990_2022,
    x="year",
    y="emissions",
    color="country",
    title="Emissions Over Time by Country",
)
fig_chart.show()
