# -*- coding: utf-8 -*-
"""Gera chas.html (e-book 'Chás do Método Desparasitação Descomplicada'). Uso: python build.py"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))

CARE_GEN = "Evite durante a <b>gravidez</b>, a <b>amamentação</b> e em <b>menores de 18 anos</b>."

TEAS = [
 dict(n=1, slug='alho', nome='Chá de alho', pop='Alho', cient='Allium sativum L.', parte='Dentes do bulbo',
  metodo='Planta de uso popular na desparasitação',
  serve='Na tradição popular, o alho é usado em preparos caseiros contra <b>vermes intestinais</b> e para aliviar <b>tosse e rouquidão</b> em resfriados.',
  preps=[dict(t='Infusão', stats=[('1 dente','cerca de 3 g, amassado'),('200 mL','água fervente'),('10 min','de descanso')],
              txt='Amasse levemente <b>1 dente de alho (cerca de 3 g)</b>. Despeje <b>200 mL de água fervente</b>, tampe, deixe descansar por <b>10 minutos</b> e coe.'),
         dict(t='Decocção', stats=[('2 a 3 dentes','cerca de 6 a 9 g'),('200 mL','água fria'),('5 a 10 min','fervura branda')],
              txt='Coloque <b>2 a 3 dentes de alho levemente amassados (cerca de 6 a 9 g)</b> em <b>200 mL de água fria</b>. Leve ao fogo. Quando ferver, abaixe o fogo e deixe em fervura branda por <b>5 a 10 minutos</b>. Desligue e coe.')],
  dose=[('200 mL','por vez'),('2×','ao dia'),('21 dias','de uso')], dose_note='O método prevê 200 mL, 2 vezes ao dia, por 21 dias.',
  care=CARE_GEN+' Se usa <b>anticoagulante</b> ou tem <b>cirurgia marcada</b>, converse com a equipe de saúde antes de usar. Se sentir enjoo ou dor no estômago, suspenda.'),
 dict(n=2, slug='boldo', nome='Chá de boldo', pop='Boldo-brasileiro e boldo-do-chile', cient='Plectranthus barbatus Andrews e Peumus boldus Molina', parte='Folhas secas',
  metodo='Suporte digestivo',
  serve='Os dois boldos têm uso tradicional para <b>má digestão e sensação de peso no estômago</b>.',
  preps=[dict(t='Infusão · Boldo-brasileiro', stats=[('1 a 3 g','folhas secas'),('200 mL','água fervente'),('15 min','em infusão')],
              txt='Use <b>1 a 3 g de folhas secas</b> em <b>200 mL de água fervente</b>. Tampe, deixe em infusão por <b>15 minutos</b>, coe e beba.'),
         dict(t='Infusão · Boldo-do-chile', stats=[('1 a 2 g','folhas secas picadas'),('200 mL','água fervente'),('10 min','em infusão')],
              txt='Use <b>1 a 2 g de folhas secas picadas</b> em <b>200 mL de água fervente</b>. Tampe, deixe em infusão por 10 minutos, coe e beba.')],
  dose=[('200 mL','por vez'),('2×','ao dia'),('até 14 dias','de uso')], dose_note='',
  care=CARE_GEN+' Quem tem <b>obstrução dos canais da bile</b> deve evitar os dois. Quem tem <b>pedra na vesícula</b> ou <b>doença no fígado</b> deve evitar o boldo-do-chile.'),
 dict(n=3, slug='milho', nome='Chá de cabelo de milho', pop='Cabelo de milho', cient='Zea mays', parte='Fios secos da espiga',
  metodo='Suporte urinário',
  serve='É usado tradicionalmente para <b>o sistema urinário, dores quando for urinar, dificuldade de urinar</b>.',
  preps=[dict(t='Infusão', stats=[('4 a 8 g','fios secos picados'),('200 mL','água fervente'),('10 min','em infusão')],
              txt='Coloque <b>4 a 8 g de fios secos picados</b> em uma xícara. Despeje <b>200 mL de água fervente</b>, tampe, deixe em infusão por <b>10 minutos</b>, coe e beba.')],
  dose=[('200 mL','por vez'),('3×','ao dia'),('14 dias','avalie se persistir')], dose_note='Se os sintomas persistirem após 14 dias, procure avaliação.',
  care=CARE_GEN+' Evite também se recebeu orientação para <b>restringir líquidos</b>. Em caso de <b>febre, dor ao urinar ou sangue na urina</b>, procure atendimento.'),
 dict(n=4, slug='cardo', nome='Chá de cardo-mariano', pop='Cardo-mariano ou cardo-de-leite', cient='Silybum marianum', parte='Frutos secos',
  metodo='Suporte hepático e digestivo',
  serve='Na fitoterapia popular, o cardo-mariano é usado como <b>apoio à função do fígado</b> e para aliviar <b>má digestão e sensação de estômago cheio</b>, aquele peso depois de comer.',
  preps=[dict(t='Infusão', stats=[('1 colher de chá','rasa, frutos moídos'),('200 mL','água fervente'),('10 min','de descanso')],
              txt='Coloque <b>1 colher de chá rasa de frutos secos moídos</b> em uma xícara. Despeje <b>200 mL de água fervente</b>, tampe, deixe descansar por <b>10 minutos</b>, coe e beba.')],
  dose=[('200 mL','por vez'),('2×','ao dia'),('21 dias','de uso')], dose_note='O método prevê 200 mL, 2 vezes ao dia, por 21 dias. Se o desconforto piorar ou persistir, procure avaliação.',
  care=CARE_GEN+' Se já teve <b>reação alérgica ao cardo-mariano</b>, evite o chá. Se sentir enjoo, dor no estômago ou diarreia após tomar, suspenda o uso.'),
 dict(n=5, slug='carqueja', nome='Chá de carqueja', pop='Carqueja ou carqueja-amarga', cient='Baccharis trimera', parte='Caules secos',
  metodo='Suporte digestivo e pancreático',
  serve='É uma planta amarga usada tradicionalmente para <b>má digestão</b>, desconforto depois de comer e auxilia em casos de diabetes tipo 2.',
  preps=[dict(t='Decocção', stats=[('1 colher de chá','cheia, carqueja seca picada'),('200 mL','água'),('5 min','de fervura')],
              txt='<b>1 colher de chá cheia de carqueja seca picada</b> em <b>200 mL de água</b>. Leve ao fogo, ferva por <b>5 minutos</b>, coe e beba.')],
  dose=[('200 mL','por vez'),('3×','ao dia'),('antes','das refeições')], dose_note='Se a má digestão persistir, procure avaliação.',
  care=CARE_GEN+' A carqueja pode <b>baixar a pressão e a glicose</b>. Se usa remédios para pressão alta ou diabetes, use com moderação.'),
 dict(n=6, slug='cravo', nome='Chá de cravo-da-índia', pop='Cravo-da-índia', cient='Syzygium aromaticum', parte='Botões florais secos',
  metodo='Desparasitação e suporte digestivo',
  serve='O cravo é usado popularmente para <b>gases e desconforto digestivo</b> e desparasitação.',
  preps=[dict(t='Infusão', stats=[('4 a 5','cravos inteiros'),('200 mL','água fervente'),('10 min','de descanso')],
              txt='Coloque <b>4 a 5 cravos inteiros</b> em <b>200 mL de água fervente</b>. Tampe, deixe descansar por <b>10 minutos</b> e coe.')],
  dose=[('após','as refeições principais'),('sem','número de dias fixo')], dose_note='A receita consultada descreve o uso após as refeições principais, sem fixar um número de dias.',
  care='Evite o uso medicinal durante a <b>gravidez</b>, a <b>amamentação</b> e em <b>menores de 18 anos</b> no método. Se sentir irritação no estômago, suspenda. Para o chá, use os <b>cravos inteiros</b>. A ingestão de <b>óleo essencial</b> de cravo pode causar intoxicação em doses altas.'),
 dict(n=7, slug='dente', nome='Chá de dente-de-leão', pop='Dente-de-leão', cient='Taraxacum officinale', parte='Raiz seca',
  metodo='Suporte digestivo e urinário',
  serve='A raiz tem uso tradicional para <b>digestão lenta, sensação de estômago cheio, azias e estufamentos</b>, e auxilia o sistema urinário.',
  preps=[dict(t='Decocção', stats=[('2 g','raiz seca picada'),('200 mL','água fria'),('10 min','de repouso')],
              txt='Coloque <b>2 g de raiz seca picada</b> em <b>200 mL de água fria</b>. Aqueça devagar até ferver, desligue, deixe repousar por <b>10 minutos</b> e coe.')],
  dose=[('200 mL','por porção'),('2 a 3×','ao dia'),('14 dias','de uso')], dose_note='',
  care=CARE_GEN+' Evite também se tem <b>pedra na vesícula</b>, obstrução dos canais da bile ou doença no fígado.'),
 dict(n=8, slug='erva', nome='Erva-de-santa-maria', pop='Erva-de-santa-maria ou mastruz', cient='Dysphania ambrosioides', parte='Folhas',
  metodo='Planta de uso popular na desparasitação',
  serve='É uma planta tradicionalmente usada contra <b>vermes intestinais</b>.',
  preps=[dict(t='Registro tradicional', stats=[('2 colheres de sopa','folhas frescas (ou 1 de secas)'),('300 mL','de água'),('10 min','em infusão')],
              steps=['<b>Ferva a água:</b> coloque os 300 mL de água em uma panela e leve ao fogo até ferver.',
                     '<b>Adicione as folhas:</b> 2 colheres de sopa de folhas frescas picadas (ou 1 colher de sopa de folhas secas). Assim que a água entrar em ebulição, desligue o fogo e adicione as folhas.',
                     '<b>Deixe em infusão:</b> tampe a panela e deixe descansar por cerca de 10 minutos.',
                     '<b>Coe:</b> coe o líquido e sirva (pode ser consumido quente ou gelado, sem adição de açúcar).'])],
  dose=[('300 mL','por vez'),('2×','ao dia'),('3 a 5 dias','de preferência na lua cheia')], dose_note='',
  care='Evite o uso caseiro do chá e do <b>óleo essencial</b>, especialmente na <b>gravidez</b>, na <b>amamentação</b> e em <b>menores de 18 anos</b>.'),
 dict(n=9, slug='losna', nome='Chá de losna', pop='Losna ou absinto', cient='Artemisia absinthium L.', parte='Folhas e pontas floridas secas',
  metodo='Suporte digestivo e auxilia na desparasitação',
  serve='É uma planta amarga usada tradicionalmente para <b>desconforto digestivo</b>. Também tem histórico de uso popular contra vermes.',
  preps=[dict(t='Infusão', stats=[('1 colher de chá','folhas secas de losna'),('fogo desligado','não ferva as folhas'),('5 a 10 min','em infusão')],
              steps=['Ferva a água, desligue o fogo e adicione <b>1 colher de chá de folhas secas de losna</b>. <b>Não ferva as folhas junto com a água</b>, para evitar a liberação excessiva de substâncias fortes e amargas.',
                     '<b>Tempo de repouso:</b> tampe o recipiente e deixe em infusão entre 5 a 10 minutos.',
                     '<b>Coar:</b> coe a bebida e aguarde amornar antes de beber.'])],
  dose=[('200 mL','por vez'),('2×','ao dia'),('15 dias','de uso')], dose_note='',
  care=CARE_GEN+' Quem tem <b>doença no fígado</b> ou obstrução dos canais da bile deve evitar. Evite ingerir o <b>óleo essencial</b>.'),
 dict(n=10, slug='oregano', nome='Chá de orégano', pop='Orégano', cient='Origanum vulgare L.', parte='Folhas frescas',
  metodo='Suporte digestivo, possui forte ação bactericida, antifúngica e antiviral',
  serve='Na fitoterapia popular, o chá de orégano é usado para <b>má digestão e gases</b>.',
  preps=[dict(t='Infusão', stats=[('1 colher de sopa','folhas frescas'),('200 mL','água fervente'),('tampe','deixe em infusão e coe')],
              txt='Coloque <b>1 colher de sopa de folhas frescas</b> em uma xícara. Despeje <b>200 mL de água fervente</b>, tampe, deixe em infusão e coe.')],
  dose=[('2 a 3×','ao dia'),('7 dias','de uso')], dose_note='',
  care='No método, a ficha é para <b>adultos a partir de 18 anos</b>. Para preparar o chá, use as folhas.'),
 dict(n=11, slug='tomilho', nome='Chá de tomilho', pop='Tomilho', cient='Thymus vulgaris L.', parte='Folhas e pontas floridas secas',
  metodo='Uso respiratório tradicional, imunidade, contribui para aliviar a digestão lenta, o inchaço abdominal e os gases',
  serve='O tomilho é usado tradicionalmente para <b>ajudar a soltar o catarro</b> na tosse associada a resfriados e sintomas digestivos.',
  preps=[dict(t='Infusão', stats=[('1 a 2 g','tomilho seco picado'),('200 mL','água fervente'),('tampe','deixe em infusão e coe')],
              txt='Coloque <b>1 a 2 g de tomilho seco picado</b> em uma xícara. Despeje <b>200 mL de água fervente</b>, tampe, deixe em infusão e coe. A quantidade de planta é a mesma da referência de 150 mL, com mais água no preparo da ficha.')],
  dose=[('3 a 4','porções de 150 mL ao dia'),('7 dias','se a tosse persistir, avalie')], dose_note='A referência descreve 3 a 4 porções de 150 mL ao dia para tosse com catarro. Se a tosse persistir por mais de 7 dias, procure avaliação.',
  care='Evite o uso medicinal durante a <b>gravidez</b>, a <b>amamentação</b> e em <b>menores de 18 anos</b> no método. Se já teve <b>reação alérgica ao tomilho</b>, evite o chá.'),
]

COMP = [
 dict(n='A', slug='composto1', nome='Chá de cardo-mariano e dente-de-leão', metodo='Suporte hepático e digestivo',
  plants=[('Cardo-mariano','Silybum marianum (L.) Gaertn.','Frutos secos triturados'),('Dente-de-leão','Taraxacum officinale F.H. Wigg.','Raiz seca picada')],
  serve='O cardo-mariano é usado tradicionalmente como <b>apoio à função do fígado</b> e para aliviar a sensação de estômago cheio. A raiz de dente-de-leão entra na mesma xícara pelo seu uso tradicional para <b>digestão lenta e desconforto depois de comer</b>.',
  ing=[('1 colher de chá','rasa de cardo-mariano'),('1 colher de chá','rasa de raiz de dente-de-leão'),('250 mL','de água')],
  prep=dict(t='Decocção seguida de infusão', steps=['Coloque a <b>raiz de dente-de-leão</b> nos <b>250 mL de água fria</b> e aqueça até começar a ferver.','Desligue o fogo e acrescente o <b>cardo-mariano</b> à mesma água.','Tampe, deixe repousar por <b>10 minutos</b> e coe.']),
  dose=[('1','preparo por dia, pela manhã'),('21 dias','início 3 dias antes da lua nova, conforme o calendário do método')], dose_note='',
  care='Evite na <b>gravidez</b>, na <b>amamentação</b> e em <b>menores de 18 anos</b>. Quem tem <b>pedra na vesícula</b>, obstrução das vias biliares ou doença no fígado deve evitar o uso por conta própria. Se o desconforto piorar ou persistir por duas semanas, procure avaliação.'),
 dict(n='B', slug='composto2', nome='Chá composto de cravo, alho e hortelã', metodo='Preparação inspirada no uso popular de plantas',
  plants=[], serve='',
  ing=[('6','cravos-da-índia inteiros'),('1 dente','de alho levemente amassado'),('1 colher de café','rasa de hortelã seca'),('250 mL','de água')],
  prep=dict(t='Infusão', steps=['Coloque o <b>cravo, o alho e a hortelã</b> em uma xícara.','Despeje a <b>água fervente</b>, tampe, deixe repousar por <b>10 minutos</b> e coe.']),
  dose=[('3×','ao dia'),('15 dias','início 3 dias antes da lua cheia')], dose_note='Conforme o calendário do método. O esquema de uso da mistura precisa de avaliação profissional antes de ser adotado.',
  care='Evite durante a <b>gravidez</b>, a <b>amamentação</b> e em <b>menores de 18 anos</b>. Se usa <b>anticoagulante</b> ou tem <b>cirurgia marcada</b>, converse com a equipe de saúde antes de usar.'),
]

THUMBS = {'Boldo':'boldo','Cardo-mariano':'cardo','Carqueja':'carqueja','Cravo-da-índia':'cravo','Dente-de-leão':'dente','Losna':'losna','Orégano':'oregano','Alho':'alho','Erva-de-santa-maria':'erva','Cabelo de milho':'milho','Tomilho':'tomilho'}

LOGO_O = '<span class="lg"><img src="img/icone-laranja.svg" alt=""><img src="img/texto-laranja.svg" alt="Desparasitação Descomplicada"></span>'
WARN = '<svg viewBox="0 0 24 24" class="ci"><path d="M12 3l10 18H2L12 3zM12 10v5M12 18v.1"/></svg>'


def head():
    return '<div class="top">%s<span>Chás do Método</span></div>' % LOGO_O


def foot(n):
    return '<div class="foot"><span>Conteúdo educativo. Não substitui avaliação profissional.</span><b>%s</b></div>' % n


def stats(items, cls=''):
    return '<div class="stats %s">' % cls + ''.join('<div class="st"><b>%s</b><span>%s</span></div>' % (a, b) for a, b in items) + '</div>'


def dose(items, note):
    s = '<div class="dose">' + ''.join('<div class="ds"><b>%s</b><span>%s</span></div>' % (a, b) for a, b in items) + '</div>'
    if note:
        s += '<p class="dnote">%s</p>' % note
    return s


def care(txt):
    return '<div class="care">%s<div><h4>Cuidados</h4><p>%s</p></div></div>' % (WARN, txt)


def prep_block(p):
    out = '<div class="prep"><h4><i></i>Como preparar <em>· %s</em></h4>' % p['t']
    out += stats(p['stats'])
    if 'steps' in p:
        out += '<ol class="steps">' + ''.join('<li>%s</li>' % s for s in p['steps']) + '</ol>'
    else:
        out += '<p>%s</p>' % p['txt']
    return out + '</div>'


def tea_page(t, pg):
    two = len(t['preps']) > 1
    meta = ('<div class="meta"><div><label>Nome popular</label><p>%s</p></div>'
            '<div><label>Nome científico</label><p class="sci">%s</p></div>'
            '<div><label>Parte usada</label><p>%s</p></div></div>') % (t['pop'], t['cient'], t['parte'])
    body = '<div class="sec"><h4><i></i>Para que serve</h4><p>%s</p></div>' % t['serve']
    body += ''.join(prep_block(p) for p in t['preps'])
    body += '<div class="sec"><h4><i></i>Frequência e duração</h4>%s</div>' % dose(t['dose'], t['dose_note'])
    body += care(t['care'])
    cls = 'tea two' if two else 'tea'
    return ('<section class="page %s">%s<div class="num">%02d</div><div class="blob"></div>'
            '<img class="ill" src="img/%s.jpg" alt=""><div class="tt"><h1>%s</h1><span class="tag">%s</span>%s</div>'
            '<div class="body">%s</div>%s</section>') % (cls, head(), t['n'], t['slug'], t['nome'], t['metodo'], meta, body, foot(pg))


def comp_page(t, pg):
    plants = ''.join('<div class="cp"><b>%s</b><span class="sci">%s</span><em>%s</em></div>' % p for p in t['plants'])
    pl = ('<div class="sec"><h4><i></i>Plantas e partes usadas</h4><div class="cps">%s</div></div>' % plants) if plants else ''
    sv = ('<div class="sec"><h4><i></i>Para que serve</h4><p>%s</p></div>' % t['serve']) if t['serve'] else ''
    pr = t['prep']
    body = pl + sv
    body += '<div class="sec"><h4><i></i>Ingredientes para 1 preparo</h4>%s</div>' % stats(t['ing'], 'four' if len(t['ing']) == 4 else '')
    body += '<div class="prep"><h4><i></i>Como preparar <em>· %s</em></h4><ol class="steps">%s</ol></div>' % (pr['t'], ''.join('<li>%s</li>' % s for s in pr['steps']))
    body += '<div class="sec"><h4><i></i>Frequência e uso propostos no método</h4>%s</div>' % dose(t['dose'], t['dose_note'])
    body += care(t['care'])
    return ('<section class="page tea comp">%s<div class="num">%s</div><div class="blob"></div>'
            '<img class="ill" src="img/%s.jpg" alt=""><div class="tt"><span class="kick">Chá composto %s</span><h1>%s</h1><span class="tag">%s</span></div>'
            '<div class="body">%s</div>%s</section>') % (head(), t['n'], t['slug'], t['n'], t['nome'], t['metodo'], body, foot(pg))


def thumbs_for(names):
    return ''.join('<span class="pt"><img src="img/%s.jpg" alt="">%s</span>' % (THUMBS[n], n) for n in names)


CSS = open(os.path.join(HERE, 'chas.css'), encoding='utf-8').read()

pages = []
pages.append('''<section class="page cover">
  <div class="arch"></div>
  <div class="cl">%s</div>
  <img class="hero" src="img/capa.jpg" alt="">
  <div class="ct"><span class="pill">E-book</span><h1>Chás do <em>Método</em></h1><p class="ds">Desparasitação Descomplicada</p>
  <p class="cs">Fichas de preparo de 11 plantas e 2 chás compostos, com ilustrações, doses e cuidados.</p></div>
  <div class="cb"><div><b>Luís Manoel</b><span>Terapeuta naturopata integrativo</span></div><div class="cn"><b>11</b> chás <i>+</i> <b>2</b> compostos</div></div>
</section>''' % LOGO_O)

rows = [('Suporte digestivo', ['Boldo', 'Cardo-mariano', 'Carqueja', 'Cravo-da-índia', 'Dente-de-leão', 'Losna', 'Orégano']),
        ('Suporte hepático', ['Cardo-mariano']), ('Suporte urinário', ['Cabelo de milho', 'Dente-de-leão']),
        ('Uso popular na desparasitação', ['Alho', 'Erva-de-santa-maria', 'Losna', 'Cravo-da-índia']),
        ('Uso respiratório tradicional', ['Alho', 'Tomilho'])]
tab = ''.join('<div class="tr"><label>%s</label><div class="pts">%s</div></div>' % (a, thumbs_for(b)) for a, b in rows)
pages.append('''<section class="page prepar">
  %s
  <span class="kick">Antes de começar</span><h1>Como <em>preparar</em></h1>
  <p class="lead">O volume de preparo é <b>200 mL de água</b>. Siga o tempo indicado na ficha de cada planta.</p>
  <div class="how">
    <div class="hc"><img src="img/infusao.jpg" alt=""><h3>Infusão</h3><p>Despeje a água fervente sobre a planta, tampe, deixe descansar e coe.</p></div>
    <div class="hc"><img src="img/decoccao.jpg" alt=""><h3>Decocção</h3><p>Leve a planta ao fogo junto com a água e siga o tempo indicado na ficha.</p></div>
  </div>
  <h2>Finalidade <em>na aula</em></h2>
  <div class="tab">%s</div>
  <div class="note"><b>Em todas as fichas:</b> evite durante a gravidez, a amamentação e em menores de 18 anos, e converse com a equipe de saúde se usa medicamentos.</div>
  %s
</section>''' % (head(), tab, foot(2)))

pg = 3
for t in TEAS:
    pages.append(tea_page(t, pg)); pg += 1
for t in COMP:
    pages.append(comp_page(t, pg)); pg += 1

doc = '''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>Chás do Método Desparasitação Descomplicada</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>%s</style></head><body>
%s
</body></html>''' % (CSS, '\n'.join(pages))
open(os.path.join(HERE, 'chas.html'), 'w', encoding='utf-8').write(doc)
print('ok', len(pages), 'paginas')
