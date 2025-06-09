from preswald import connect, get_df, query, plotly, sidebar
import pandas as pd
import plotly.express as px

sidebar(True, name="Game Sales Analysis")  # Initialize sidebar for the analysis
connect()  # Initialize connection to preswald.toml data sources
df = get_df("vgsales")  # Load the DataFrame from the specified source




sql = """SELECT 
            title as 'Title',
            console as 'Platform',
            critic_score as 'Critic Score',
            total_sales as 'Sales',
            na_sales as 'NA Sales',
            jp_sales as 'JP Sales',
        FROM vgsales 
        WHERE TRY_CAST(total_sales AS INTEGER) >= 1 AND TRY_CAST(critic_score AS INTEGER) >= 0
        
        
        
        """  # SQL query to filter data
filtered_df = query(sql, "vgsales")  # Execute SQL query to filter data

from preswald import table, text

text("# Game Sales Analysis")  
text("### Games Sales over 1 Million")  
table(filtered_df, title="Filtered Data")

# table(filtered_df["Critic Score"])

fig = px.scatter(filtered_df,
                 y=filtered_df["Critic Score"].apply(pd.to_numeric),
                 x=filtered_df["Sales"].sort_values(ascending=False).apply(pd.to_numeric),
                #  x="Sales",
                #  color="Platform",
                 hover_name="Title",
                 title="Game Sales vs Critic Score",
                 labels={"x": "Total Sales (in millions)", "y": "Critic Score", "Platform": "Platform"},
                 )
# fig.show()
plotly(fig)

