import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def get_image():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_the_plot(chart_type,*args,**kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(15,10))

    x = kwargs.get('x')
    y = kwargs.get('y')
    data =kwargs.get('data')
    # df = kwargs.get('df')
    if chart_type == 'bar':
        title = 'Bar Plot'
        plt.title(title)
        plt.bar(x,y)
    elif chart_type == 'line':
        title = 'Line Plot'
        plt.title(title)
        plt.plot(x,y)
    else:
        title ='Count Plot'
        plt.title(title)
        sns.countplot('name',data=data)
    plt.tight_layout()
    
    graph = get_image()
    return graph