from django import forms #forms padrao do django

class TarefaForm(forms.Form):

    tarefa = forms.CharField(
        max_length=100,
        required=True, #torna o preenchimento obrigatório
        widget= forms.TextInput(attrs = {
            'id':'id_tarefa',
            'class':"form-control",
            'placeholder':'Digite sua tarefa...'
        })
    )