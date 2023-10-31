'''''# Importação de módulos e funções necessários
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views.generic import TemplateView
from .form import ContatoForm

# Definição de uma classe baseada em TemplateView
class PDFGeneratorView(TemplateView):
    template_name = 'form.html'  # Substitua 'seu_template.html' pelo caminho correto

    # Método para adicionar o formulário ao contexto da view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContatoForm()
        return context

    # Método para lidar com uma requisição POST
    def post(self, request):
        form = ContatoForm(request.POST)

        if form.is_valid():
            # Extração dos dados do formulário
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            opcoes = form.cleaned_data['opcoes']
            horario = form.cleaned_data['horario']
            local = form.cleaned_data['local']
          
            # Renderização do template HTML com os dados do formulário
            template = get_template(self.template_name)
            context = {
                'nome': nome,
                'email': email,
                'opcoes': opcoes,
                'horario': horario,
                'local': local,
            }
            html = template.render(context)

            # Criação de uma resposta HTTP do tipo PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="comprovante.pdf"'

            # Uso do xhtml2pdf para criar o PDF a partir do HTML
            pisa_status = pisa.CreatePDF(html, dest=response)

            if not pisa_status.err:
                # Envio de e-mail com o PDF anexado
                subject = 'Comprovante de Agendamento'
                message = 'Segue o comprovante de Agendamento em anexo.'
                from_email = settings.DEFAULT_FROM_EMAIL  # E-mail padrão definido nas configurações
                recipient_list = [email]
                email = EmailMessage(subject, message, from_email, recipient_list)
                email.attach('comprovante.pdf', response.getvalue(), 'application/pdf')
                email.send()

                return render(request, 'index.html')  # Redirecionamento para uma página de sucesso
            else:
                return HttpResponse('Ocorreu um erro ao gerar o PDF')
        else:
            context = {'form': form}
            return render(request, self.template_name, context)
'''












''




def i(request):
     return render(request, 'index.html')








#essa view de baixo esta funcinando



from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from xhtml2pdf import pisa 
from django.views.generic import TemplateView

from .form import ContatoForm

#from .models import DadosFormModels



def contato(request):
     if str(request.method) == 'POST':
          form = ContatoForm(request.POST)
          if form.is_valid():
               form.send_email()
               form = ContatoForm()
     else:
          form = ContatoForm()
     context = {
          'form' : form
     }
     return render(request, 'form.html', context)
               








'''
def enviar_email(request):
    if request.method == 'POST':
          form = DadosFormModels(request.POST)
          # Obtenha os dados do formulário
          nome = request.POST.get('nome')
          email = request.POST.get('email')
          mensagem = request.POST.get('mensagem')

          # Crie o conteúdo do e-mail a partir de um modelo HTML (opcional)
          html_message = render_to_string('email_template.html', {'nome': nome, 'mensagem': mensagem})
          plain_message = strip_tags(html_message)

        # Envie o e-mail
          send_mail(
               'Assunto do E-mail',
               plain_message,
               settings.DEFAULT_FROM_EMAIL,  # Remetente
               [email],  # Destinatário(s), pode ser uma lista de endereços de e-mail
               html_message=html_message,  # Conteúdo HTML (opcional)
          )

          # Redirecione ou retorne uma resposta de sucesso
          return redirect('sucesso')  # Redirecione para a página de sucesso
          # Ou retorne uma resposta de sucesso
          # return HttpResponse("E-mail enviado com sucesso!")

    return render(request, 'form.html')  # Renderize o formulário
'''







'''from django.shortcuts import render, redirect
from django.views.generic import TemplateView,CreateView
from .form import DadosForm
from .models import DadosFormModels
from django.urls import reverse_lazy

def index(request):
     if request.method == 'POST':
          form = DadosFormModels(request.POST)
          if form.is_valid():
               form.save()
               return redirect('index')
          
     else:
          form = DadosFormModels()
          return render(request,'form.html',{
        'form':form
        })
     return render(request, 'form.html', {'from':form})'''