# **Traffic Accident Analysis on Calle 30 in Barranquilla**

This project provides a detailed analysis of traffic accidents recorded on Calle 30 in Barranquilla, Colombia, using data from the [Open Data Portal of Colombia](https://www.datos.gov.co/). The objective is to identify annual trends, critical months, hourly patterns, and variations in accident severity.  

## **Data Sources**  
The data used for this analysis is publicly available at [Traffic Accidents Barranquilla Calle 30](https://www.datos.gov.co/Transporte/accidentes-calle-30-2015-2019/sefb-a755). The dataset covers the period from 2015 to May 2020.  

## **Analysis Objectives**  

1. **Identification of Temporal Trends:**  
   - Analyze the quarterly evolution of traffic accidents recorded on Calle 30 in Barranquilla from 2015 to 2019 to uncover significant occurrence patterns.  

2. **Distribution by Time of Day:**  
   - Examine how the number of accidents varies throughout the day, categorizing the timeframes into morning, afternoon, peak hours, and off-peak hours to evaluate their influence on incident frequency.  

3. **Seasonal and Weekly Variability:**  
   - Assess the dispersion of traffic accidents by day of the week and quarter using graphical analysis tools such as `boxplots` within a `FacetGrid`.  

## **Technologies Used**  

1. **Python:** The primary language for data processing and visualization.  
2. **Pandas:** Advanced data manipulation, metric creation, and segmentation for analysis.  
3. **Seaborn:** Statistical graphics design, including `lineplot`, `FacetGrid`, and `boxplot` for exploring trends and variations in the data.  
4. **Matplotlib:** Detailed customization of visualizations to enhance presentation and clarity.  

## **Generated Visualizations**  

1. **`Lineplot` Chart (Quarterly Accident Analysis):**  
   - Represents the total number of accidents per quarter from 2015-2019, highlighting trends and critical points over time.  

2. **`Lineplot` Chart (Hourly Distribution):**  
   - Displays how accidents are distributed across different time categories (morning, afternoon, peak hours, off-peak hours), identifying high-risk periods.  

3. **`FacetGrid` with `Boxplot` (Quarterly and Weekly Variability):**  
   - Presents the variability of accidents across days of the week and quarters using a visual approach that highlights data dispersion and concentrations.  

## **Key Findings**  

### **Insights on Accident Variability:**  
1. Historically, there is a slight increase in daily accidents during the **morning work hours** compared to the afternoon.  
2. In January, June, and December, the average number of daily accidents is similar for both morning and afternoon, indicating stability during these months.  
3. In April, data shows that approximately 50% of the morning accidents represent 75% of those recorded in the afternoon.  
4. In May and July, the afternoon surpasses the morning in daily accident averages, standing out as the only months with this behavior.  
5. The months **March, February, May, April, and November** recorded the highest number of accidents during the analyzed period (2015-2020).  

### **Temporal and Hourly Insights:**  
1. **Quarterly Trends:** The last quarter of the year consistently records the highest number of accidents, showing a progressive increase from the first to the fourth quarter.  
2. **Hourly Distribution:** Peak accident hours are between **2:00 PM and 5:59 PM**, followed by spikes during morning work hours and off-peak periods.  
3. Regarding weekly and hourly patterns, **Fridays in Q3 of 2016** had the highest average number of accidents per month, while **Sundays in Q3 of 2019** recorded the lowest average.  

These observations reinforce the hypothesis of a progressive and sustained increase in accident frequency as the year progresses. This trend can be attributed to multiple factors, such as weather conditions, commercial activity, or mass commuting patterns.  

## **Installation and Usage**  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your_username/traffic-accidents-calle-30-barranquilla.git  
   ```  

## **Author**  
**Somil Sandoval Díaz**  
Systems and Computer Engineering, Universidad del Norte.  