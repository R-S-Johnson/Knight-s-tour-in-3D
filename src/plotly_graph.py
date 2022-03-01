import plotly.graph_objects as go
from Algorithm import KnightsTour




for i in range(8):
    for j in range(8):
        for k in range(8):
            n = 8
            runner = KnightsTour(n)
            x = []
            y = []
            z = []
            newPoint = runner.initialize(i, j, k)
            x.append(newPoint[0])
            y.append(newPoint[1])
            z.append(newPoint[2])

            for n in range(n**3):
                newPoint = runner.takeStep()
                if newPoint == None:
                    break
                x.append(newPoint[0])
                y.append(newPoint[1])
                z.append(newPoint[2])


if len(x) == 512:
    fig = go.Figure(data=go.Scatter3d(
        x=x, y=y, z=z,
        line=dict(
            color='red',
            width=2
        ),
        marker=None
    ))
    fig.show()
else:
    print("no solution found in time alotted")