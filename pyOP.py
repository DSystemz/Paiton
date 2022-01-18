# INICIO PRODUÇÃO
# pedidos finalizados por dia
# meta minima
# meta maxima
# lucro diario
# estimativa de lucro mensal
# FIM PRODUÇÃO
# =============================================
# INICIO GESTÃO
# envio de arquivo com dados 
# gerar relatório para impressão
# opção para arquivar relatório ou apagar
# FIM GESTÃO

from datetime import date, datetime
import os
from fpdf import FPDF

def PedidosF():
    while PedidosF:
        print ("O pedido ainda não foi iniciado, por favor digite as informações.")
        valor = str(input('Digite o valor da O.D ===> '))
        OD = int(input("Digite o número da O.D ===> "))
        OP = str(input("Digite o pimeiro nome do Operador ==> "))
        dt = date.today()
        txt = ('{}/{}/{}'.format(dt.day, dt.month, dt.year))
        print(txt)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font('arial', 'B', 13.0)
        pdf.cell(ln=0, h=5.0, align='L', w=0, txt="VALOR: {} \n O.D: {} \n OPERADOR: {}".format(valor, OD, OP), border=0)
        pdf.output('Relatorio.pdf', 'F')
        break
PedidosF()