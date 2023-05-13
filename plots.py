import plotly.express as px
import plotly.graph_objects as go


def main():

    # Declare data
    data = {
        "i": [0.430, 5.430, 10.00, 14.57, 15.00],
        "v": [3.000, 38.00, 70.00, 102.0, 105.0],
        "r": [7, 7, 7, 7, 7]
    }

    # Declare axis
    y = [v / i for v, i in zip(data["v"], data["i"])]
    x = data["v"]

    # Set points
    fig = px.scatter(x=x,
                  y=y,
                  title="Voltaje en función del voltaje sobre la intensidad")
    fig.update_xaxes(title_text="Intensidad")
    fig.update_yaxes(title_text="Voltaje")

    # Create a new trace with a curvy line and markers for all data points
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines+markers",
            line=dict(shape='spline', color="#7FB3D5"),
            showlegend=False,
        )
    )

    # Update the y-axis range
    fig.update_layout(yaxis=dict(range=[0, 10]), template='plotly_dark')

    # Export image
    fig.write_image('Voltaje en función del voltaje sobre la intensidad.png', width=1000, height=1000)

main()
