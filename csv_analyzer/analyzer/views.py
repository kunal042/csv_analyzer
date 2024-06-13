from django.shortcuts import render
import pandas as pd
from django.shortcuts import render, redirect
from .forms import CSVFileForm
from .models import CSVFile
from django.conf import settings
import os
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io



def upload_file(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('process_file', pk=form.instance.pk)
    else:
        form = CSVFileForm()
    return render(request, 'analyzer/upload.html', {'form': form})

def process_file(request, pk):
    csv_file = CSVFile.objects.get(pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, csv_file.file.name)
    data = pd.read_csv(file_path)

    # Perform basic data analysis
    head = data.head().to_html()
    description = data.describe().to_html()

    # Generate plots
    plots = []
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        sns.histplot(data[column].dropna())
        plt.title(f'Histogram of {column}')

        # Save plot to a string in base64 format
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        image_base64 = base64.b64encode(image_png).decode('utf-8')
        plots.append(image_base64)


    context = {
        'head': head,
        'description': description,
        'file': csv_file,
    }
    return render(request, 'analyzer/process.html', context)



def process_file(request, pk):
    csv_file = CSVFile.objects.get(pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, csv_file.file.name)
    data = pd.read_csv(file_path)

    # Perform basic data analysis
    head = data.head().to_html()
    description = data.describe().to_html()

    # Generate plots
    plots = []
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        sns.histplot(data[column].dropna())
        plt.title(f'Histogram of {column}')

        # Save plot to a string in base64 format
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        image_base64 = base64.b64encode(image_png).decode('utf-8')
        plots.append(image_base64)

    context = {
        'head': head,
        'description': description,
        'file': csv_file,
        'plots': plots,
    }
    return render(request, 'analyzer/process.html', context)


def contact(request):
    return render(request, 'analyzer/contact.html')