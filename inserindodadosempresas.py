#Importando a biblioteca PyMySQL

import pymysql

#Crindo conexão com o servidor local

database = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="unicamp_energy_club"
)

cursor = database.cursor()

# Inserindo dados

com_sql = "insert into empresas(nome, serviços, contato, site) values (%s, %s, %s, %s)"
valor = [("CPFL Energias Renováveis AS", "Atua no ramo da energia solar, biomassa, eolica e hidreletrica", "jornalismo@cpfl.com.br", "http://www.cpflrenovaveis.com.br/"),
         ("Canadian Solar", "Fabricante de módulos fotovoltaicos solares e um fornecedor de soluções", "Telefone: +55 11 3957-4600", "https://canadiansolar.com.br/la/"),
         ("IPERSOL", "Projetos e Instalações Fotovoltaicas", "contato@ipersol.com.br", "https://ipersol.com.br/"),
         ("NeoSol Energia", "Projetos para construção e reformas, focados na geração fotovoltaica", "contato@neosol.com.br", " http://www.neosol.com.br"),
         ("EverSun", "Painel Fotovoltaico, projeto fotovoltaico, inversor, regularização", "fabio@eversun.com.br", "http://eversun.com.br/"),
         ("Dexxtrasolar", "Serviços de Engenharia no ramo de Energias Renováveis", "contato@dexxtrasolar.com.br", " https://www.suncorp.com.br"),
         ("Proinst solar", "Estudo e dimensionamento do sistema de geração fotovoltaico", "solar@proinst.com.br", "https://www.proinst.com.br/"),
         ("SUNCORP", "Serviços e projetos na area de energia solar fotovoltaica", "atendimento@suncorp.com.br", " https://www.suncorp.com.br"),
         ("Alva energia solar", "contato@alvaengenharia.com.br", "https://www.alvaengenharia.com.br/", "Projetos, Instalação e Manutenção em Sistemas de Geração de Energia Solar."),
         ("Bom Tempo Energia Solar", "contato@bomtemposolar.com.br", "http://www.bomtemposolar.com.br", "serviços turn-key para sistemas de microgeração e minigeração de energia solar fotovoltaica para sistemas conectados à rede"),
         ("Power Supply", "comercial@powersupply.com.br", "https://www.powersupply.com.br", "Planejamento e instalação de paineis fotovoltaicos"),
         ("Casa dos Ventos", "(11) 4084-4200", "https://www.casadosventos.com.br/pt/", "Casa dos Ventos é líder no desenvolvimento de parques eólicos no Brasil."),
         ("Enel Green Power", "Tel: (55) 21 2206.5600 site: https://globalprocurement.enel.com/pt/contatos", "https://www.enelgreenpower.com/pt/paises/america-do-sul/brasil", "Empresa do Grupo Enel dedicada ao desenvolvimento e gestão da geração de energia a partir de fontes renováveis em todo o mundo."),
         ("EDF Renováveis", "(55) 21 3974-6100", "http://www.edf-renouvelables.com", "A EDF Renewables é uma empresa internacional líder em energias renováveis, com capacidade instalada bruta de 13 GW em todo o mundo."),
         ("GE", "https://www.ge.com/br/contato", "https://www.ge.com/br/", "Fornecimento de turbinas eólicas"),
         ("WEG", "info-br@weg.net", "https://www.weg.net/institutional/BR/pt/", "A WEG possui produtos e soluções para todas as fontes de energia renovável, como eólica, solar, biomassa, hidráulica (CGHs e PCHS) e resíduos (waste to energy), além de armazenamento de energia (energy storage) e infraestrutura elétrica (transformadores, seccionadoras, subestações)"),
         ("Atvos", "(11) 3096-8000", "https://www.atvos.com/", "Produzimos e comercializamos etanol, açúcar VHP e energia elétrica através da cana-de-açúcar e da biomassa."),
         ("Vestas", " ", "https://www.vestas.com/#!", "A Vestas é uma empresa dinamarquesa e a maior companhia mundial produtora de turbinas de energia eólica"),
         ("Omega", "551132549810", "http://www.omegaenergia.com.br", "Recursos renováveis e meio ambiente"),
         ("CGN Brazil Energy", "contato@atlanticenergias.com.br", "contato@atlanticenergias.com.br", "atua no desenvolvimento, implantação e operação de projetos de energia renovável."),
         ("Sunew", " ", "https://sunew.com.br/?gclid=CjwKCAjwyo36BRAXEiwA24CwGZvMrIASP0lNr4obOJ_0zIvyGhRzD0Mo-RGzGi8Sqk3bApE-KvmrVxoC_IcQAvD_BwE", "Fabricação de Painéis fotovoltaicos orgânicos no Brasil"),
cursor.executemany(com_sql, valor)

database.commit()

print(cursor.rowcount, "inserida com sucesso")
