# Consumption-based CO₂ emissions - Data package

This data package contains the data that powers the chart ["Consumption-based CO₂ emissions"](https://ourworldindata.org/grapher/consumption-co2-emissions?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website. It was downloaded on December 07, 2024.

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The final column is the data column, which is the time series that powers the chart. If the CSV data is downloaded using the "full data" option, then the column corresponds to the time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data column is transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

## Detailed information about the data


## Annual consumption-based CO₂ emissions
Annual consumption-based emissions of carbon dioxide (CO₂), measured in tonnes.
Last updated: November 21, 2024  
Next update: November 2025  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Global Carbon Budget (2024) – with major processing by Our World in Data

#### Full citation
Global Carbon Budget (2024) – with major processing by Our World in Data. “Annual consumption-based CO₂ emissions – GCB” [dataset]. Global Carbon Project, “Global Carbon Budget” [original data].
Source: Global Carbon Budget (2024) – with major processing by Our World In Data

### What you should know about this data
* Consumption-based emissions attribute the emissions generated in the production of goods and services according to where they were _consumed_, rather than where they were _produced_.
* The data is calculated by adjusting 'production-based' emissions (emissions produced domestically) for trade: Consumption-based emissions equals production-based emissions, _minus_ emissions embedded in exports, _plus_ emissions embedded in imports.
* If a country's consumption-based emissions are higher than its production emissions it is a net importer of carbon dioxide. If its consumption-based emissions are lower, then it is a net exporter.
* Consumption-based emissions are not available for all countries because not all countries have sufficient, high-quality trade data. But those without complete data are a small fraction (3%) of the global total.
* This data measures carbon dioxide (CO₂) emissions from fossil fuels and industry and does not include emissions from land use change, deforestation, soils, or vegetation.
* Emissions from international aviation and shipping are not included in any country or region's emissions. They are only included in the global total emissions.

### Source

#### Global Carbon Project – Global Carbon Budget
Retrieved on: 2024-11-21  
Retrieved from: https://globalcarbonbudget.org/  

#### Notes on our processing step for this indicator
- Data on global emissions has been converted from tonnes of carbon to tonnes of carbon dioxide (CO₂) using a conversion factor of 3.664.
- Emissions from the Kuwaiti oil fires in 1991 have been included as part of Kuwait's emissions for that year.
- Country's share of the global population is calculated using our population dataset, based on [different sources](https://ourworldindata.org/population-sources).
- Each country's share of global CO₂ emissions from flaring has been calculated using global CO₂ emissions from flaring provided in the Global Carbon Budget dataset.



    