from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime
from database import (mysql, 
                      get_perfis, get_perfil_por_id, cadastrar_perfil, editar_perfil, excluir_perfil, 
                      get_usuarios, get_usuario_por_id, cadastrar_usuario, editar_usuario, excluir_usuario, 
                      get_categorias, get_categoria_por_id, cadastrar_categoria, editar_categoria, excluir_categoria,
                      get_subcategorias, get_subcategoria_por_id, get_subcategorias_por_categoria, cadastrar_subcategoria, editar_subcategoria, excluir_subcategoria,
                      get_unidadesdemedida, get_unidadedemedida_por_id, cadastrar_unidadedemedida, editar_unidadedemedida, excluir_unidadedemedida,
                      get_locaisdacasa, get_localdacasa_por_id, cadastrar_localdacasa, editar_localdacasa, excluir_localdacasa,
                      get_produtos, get_produto_por_id, cadastrar_produto, editar_produto, excluir_produto,
                      get_estabelecimentos, get_cidades, get_estabelecimento_por_id, cadastrar_estabelecimento, editar_estabelecimento, excluir_estabelecimento,
                      get_formasdepagamento, get_formadepagamento_por_id, cadastrar_formadepagamento, editar_formadepagamento, excluir_formadepagamento,
                      get_listasdecompras, get_listadecompras_por_id, cadastrar_listadecompras, editar_listadecompras, excluir_listadecompras,
                      get_itenslistadecompras_por_id_listadecompras, cadastrar_itenslistadecompras, get_produtositens, editar_itemlistadecompras, get_itemlistadecompras_por_ids)

app = Flask(__name__)

# Conexão com o banco de dados
try:
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "control_home"
    app.config["MYSQL_PASSWORD"] = "controlhome"
    app.config["MYSQL_DB"] = "control_home"
    app.config["MYSQL_CURSORCLASS"] = "DictCursor"
    mysql.init_app(app)
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

# Rota inicial do site Control Home
@app.route("/")
def home():
    return render_template("index.html")

# Rota inicial do ambiente administrativo do site Control Home
@app.route("/admin")
def home_admin():
    return render_template("admin.html")

# Rota para tela de perfis
@app.route("/perfis")
def listar_perfis():
    lista_perfis = get_perfis()    
    return render_template("perfis.html", perfis=lista_perfis, total_items=len(lista_perfis) if len(lista_perfis) > 0 else None)

# Rota para receber os dados do formulário e cadastrar perfis no banco de dados
@app.route('/perfis/novo', methods=['POST'])
def cadastrar_perfil_route():
    if request.method == "POST":
        cadastrar_perfil(request.form['descricao'])    
    return redirect(url_for('listar_perfis'))

# Rota para editar perfis no banco de dados
@app.route('/perfis/<int:id>/editar', methods=['GET', 'POST'])
def editar_perfil_route(id):
    if request.method == 'GET':
        # Busca o perfil com o id informado no banco de dados
        perfil = get_perfil_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': perfil['ID'],
            'descricao': perfil['DESCRICAO']
        }
        # Renderiza o template de edição de perfil com os dados do perfil encontrado
        return render_template('perfis.html', item_edit=item_data)
    elif request.method == 'POST':
        editar_perfil(id, request.form['descricao_edit'])
        return redirect(url_for('listar_perfis'))
    
# Rota para excluir perfis no banco de dados
@app.route('/perfis/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_perfil_route(id):
    excluir_perfil(id)    
    return redirect(url_for('listar_perfis'))

# Rota para tela de usuários
@app.route("/usuarios")
def listar_usuarios():
    lista_usuarios = get_usuarios()    
    return render_template("usuarios.html", usuarios=lista_usuarios, total_items=len(lista_usuarios), perfis=get_perfis())

# Rota para receber os dados do formulário e cadastrar usuários no banco de dados
@app.route('/usuarios/novo', methods=['POST'])
def cadastrar_usuario_route():
    if request.method == "POST":
        cadastrar_usuario(request.form['nome'],request.form['apelido'], 
                          request.form['email'], datetime.strptime(request.form['data_nascimento'], '%d/%m/%Y').strftime('%Y-%m-%d'), 
                          request.form['perfil'], request.form['senha'])    
    return redirect(url_for('listar_usuarios'))

# Rota para editar usuarios no banco de dados
@app.route('/usuarios/<int:id>/editar', methods=['GET', 'POST'])
def editar_usuario_route(id):
    if request.method == 'GET':
        # Busca o perfil com o id informado no banco de dados
        usuario = get_usuario_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': usuario['ID'],
            'nome': usuario['NOME'],
            'apelido': usuario['APELIDO'],
            'email': usuario['EMAIL'],
            'data_nascimento': usuario['DATANASCIMENTO'].strftime('%d/%m/%Y'),
            'perfil': usuario['ID_PERFIL'],
            'senha': usuario['SENHA']
        }
        # Renderiza o template de edição de perfil com os dados do perfil encontrado
        return render_template('usuarios.html', item_edit=item_data, perfis=get_perfis())
    elif request.method == 'POST':
        editar_usuario(id, request.form['nome_edit'], request.form['apelido_edit'], request.form['email_edit'], request.form['data_nascimento_edit'], request.form['perfil_edit'], request.form['senha_edit'])
        return redirect(url_for('listar_usuarios'))
    
# Rota para excluir usuários no banco de dados
@app.route('/usuarios/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_usuario_route(id):    
    excluir_usuario(id)    
    return redirect(url_for('listar_usuarios'))

# Rota para tela de categorias
@app.route("/categorias")
def listar_categorias():
    lista_categorias = get_categorias()    
    return render_template("categorias.html", categorias=lista_categorias, total_items=len(lista_categorias))

# Rota para receber os dados do formulário e cadastrar categorias no banco de dados
@app.route('/categorias/novo', methods=['POST'])
def cadastrar_categoria_route():
    if request.method == "POST":
        cadastrar_categoria(request.form['descricao'])    
    return redirect(url_for('listar_categorias'))

# Rota para editar categorias no banco de dados
@app.route('/categorias/<int:id>/editar', methods=['GET', 'POST'])
def editar_categoria_route(id):
    if request.method == 'GET':
        # Busca a categoria com o id informado no banco de dados
        categoria = get_categoria_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': categoria['ID'],
            'descricao': categoria['DESCRICAO']
        }
        # Renderiza o template de edição de categoria com os dados da categoria encontrado
        return render_template('categorias.html', item_edit=item_data)
    elif request.method == 'POST':
        editar_categoria(id, request.form['descricao_edit'])
        return redirect(url_for('listar_categorias'))
    
# Rota para excluir categorias no banco de dados
@app.route('/categorias/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_categoria_route(id):
    excluir_categoria(id)    
    return redirect(url_for('listar_categorias'))

# Rota para tela de subcategorias
@app.route("/subcategorias")
def listar_subcategorias():
    lista_subcategorias = get_subcategorias()    
    return render_template("subcategorias.html", subcategorias=lista_subcategorias, total_items=len(lista_subcategorias), categorias=get_categorias())

# Rota para receber os dados do formulário e cadastrar subcategorias no banco de dados
@app.route('/subcategorias/novo', methods=['POST'])
def cadastrar_subcategoria_route():
    if request.method == "POST":
        cadastrar_subcategoria(request.form['categoria'], request.form['descricao'])    
    return redirect(url_for('listar_subcategorias'))

# Rota para editar subcategorias no banco de dados
@app.route('/subcategorias/<int:id>/editar', methods=['GET', 'POST'])
def editar_subcategoria_route(id):
    if request.method == 'GET':
        # Busca a subcategoria com o id informado no banco de dados
        subcategoria = get_subcategoria_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': subcategoria['ID'],
            'categoria': subcategoria['ID_Categoria'],
            'descricao': subcategoria['DESCRICAO']
        }
        # Renderiza o template de edição de subcategoria com os dados da subcategoria encontrada
        return render_template('subcategorias.html', item_edit=item_data, categorias=get_categorias())
    elif request.method == 'POST':
        editar_subcategoria(id, request.form['categoria_edit'], request.form['descricao_edit'])
        return redirect(url_for('listar_categorias'))
    
#Rota em andamento
@app.route('/subcategorias/<int:id_categoria>', methods=['GET', 'POST'])
def subcategorias_por_categoria(id_categoria):
    subcategorias = get_subcategorias_por_categoria(id_categoria)
    return jsonify(subcategorias)
    
# Rota para excluir subcategorias no banco de dados
@app.route('/subcategorias/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_subcategoria_route(id):
    excluir_subcategoria(id)    
    return redirect(url_for('listar_subcategorias'))

# Rota para tela de unidade de medida
@app.route("/unidadesdemedida")
def listar_unidadesdemedida():
    lista_unidadesdemedida = get_unidadesdemedida()    
    return render_template("unidadesdemedida.html", unidadesdemedida=lista_unidadesdemedida, total_items=len(lista_unidadesdemedida))

# Rota para receber os dados do formulário e cadastrar unidades de medida no banco de dados
@app.route('/unidadesdemedida/novo', methods=['POST'])
def cadastrar_unidadedemedida_route():
    if request.method == "POST":
        cadastrar_unidadedemedida(request.form['descricao'])    
    return redirect(url_for('listar_unidadesdemedida'))

# Rota para editar unidades de medida no banco de dados
@app.route('/unidadesdemedida/<int:id>/editar', methods=['GET', 'POST'])
def editar_unidadedemedida_route(id):
    if request.method == 'GET':
        # Busca a unidade de medida com o id informado no banco de dados
        unidadedemedida = get_unidadedemedida_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': unidadedemedida['ID'],
            'descricao': unidadedemedida['DESCRICAO']
        }
        # Renderiza o template de edição de categoria com os dados da unidade de medida encontrada
        return render_template('unidadesdemedida.html', item_edit=item_data)
    elif request.method == 'POST':
        editar_unidadedemedida(id, request.form['descricao_edit'])
        return redirect(url_for('listar_unidadesdemedida'))
    
# Rota para excluir unidades de medida no banco de dados
@app.route('/unidadesdemedida/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_unidadedemedida_route(id):
    excluir_unidadedemedida(id)    
    return redirect(url_for('listar_unidadesdemedida'))

# Rota para tela de local casa
@app.route("/locaisdacasa")
def listar_locaisdacasa():
    lista_locaisdacasa = get_locaisdacasa()    
    return render_template("locaisdacasa.html", locaisdacasa=lista_locaisdacasa, total_items=len(lista_locaisdacasa))

# Rota para receber os dados do formulário e cadastrar locais da casa no banco de dados
@app.route('/locaisdacasa/novo', methods=['POST'])
def cadastrar_localdacasa_route():
    if request.method == "POST":
        cadastrar_localdacasa(request.form['descricao'])    
    return redirect(url_for('listar_locaisdacasa'))

# Rota para editar locais da casa no banco de dados
@app.route('/locaisdacasa/<int:id>/editar', methods=['GET', 'POST'])
def editar_localdacasa_route(id):
    if request.method == 'GET':
        # Busca o loca da casa com o id informado no banco de dados
        localdacasa = get_localdacasa_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': localdacasa['ID'],
            'descricao': localdacasa['DESCRICAO']
        }
        # Renderiza o template de edição de categoria com os dados da unidade de medida encontrada
        return render_template('locaisdacasa.html', item_edit=item_data)
    elif request.method == 'POST':
        editar_localdacasa(id, request.form['descricao_edit'])
        return redirect(url_for('listar_locaisdacasa'))
    
# Rota para excluir unidades de medida no banco de dados
@app.route('/locaisdacasa/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_localdacasa_route(id):
    excluir_localdacasa(id)    
    return redirect(url_for('listar_locaisdacasa'))

# Rota para tela de produtos
@app.route("/produtos")
def listar_produtos():
    lista_produtos = get_produtos()    
    return render_template("produtos.html", produtos=lista_produtos, total_items=len(lista_produtos), categorias=get_categorias(), 
                           subcategorias=get_subcategorias(), unidadesdemedida=get_unidadesdemedida(), locaisdacasa=get_locaisdacasa())

# Rota para receber os dados do formulário e cadastrar produtos no banco de dados
@app.route('/produtos/novo', methods=['POST'])
def cadastrar_produto_route():
    if request.method == "POST":
        datavencimento = request.form['datavencimento']
        quantidadeestoque = request.form['quantidadeestoque']
        quantidademinima = request.form['quantidademinima']
        if not datavencimento: datavencimento = None
        if not quantidadeestoque: quantidadeestoque = 0
        if not quantidademinima: quantidademinima = None
        cadastrar_produto(request.form['descricao'], request.form['categoria'], request.form['subcategoria'], 
                          request.form['unidadedemedida'], request.form['localdacasa'], datavencimento,
                          quantidadeestoque, quantidademinima, request.form['perecivel'])
    return redirect(url_for('listar_produtos'))

# Rota para editar produtos no banco de dados
@app.route('/produtos/<int:id>/editar', methods=['GET', 'POST'])
def editar_produto_route(id):
    if request.method == 'GET':
        # Busca o produto com o id informado no banco de dados
        produto = get_produto_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': produto['ID'],
            'descricao': produto['DESCRICAO'],
            'categoria': produto['ID_CATEGORIA'],
            'subcategoria': produto['ID_SUBCATEGORIA'],
            'unidadedemedida': produto['ID_UNIDADEDEMEDIDA'],
            'localdacasa': produto['ID_LOCALDACASA'],
            'datavencimento': produto['DATAVENCIMENTO'],
            'quantidadeestoque': produto['QUANTIDADEESTOQUE'],
            'quantidademinima': produto['QUANTIDADEMINIMA'],
            'perecivel': produto['PERECIVEL']
        }
        # Renderiza o template de edição de categoria com os dados da categoria encontrado
        return render_template('produtos.html', item_edit=item_data, categorias=get_categorias(), subcategorias=get_subcategorias(), 
                               unidadesdemedida=get_unidadesdemedida(), locaisdacasa=get_locaisdacasa())
    elif request.method == 'POST':
        datavencimento = request.form['datavencimento_edit']
        quantidadeestoque = request.form['quantidadeestoque_edit']
        quantidademinima = request.form['quantidademinima_edit']
        if not datavencimento: datavencimento = None
        if not quantidadeestoque: quantidadeestoque = 0
        if not quantidademinima: quantidademinima = None
        editar_produto(id, request.form['descricao_edit'], request.form['categoria_edit'], 
                       request.form['subcategoria_edit'], request.form['unidadedemedida_edit'],
                       request.form['localdacasa_edit'], datavencimento,
                       quantidadeestoque, quantidademinima,
                       request.form['perecivel_edit'],)
        return redirect(url_for('listar_produtos'))
    
# Rota para excluir produtos no banco de dados
@app.route('/produtos/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_produto_route(id):
    excluir_produto(id)    
    return redirect(url_for('listar_produtos'))

# Rota para tela de estabelecimentos
@app.route("/estabelecimentos")
def listar_estabelecimentos():
    lista_estabelecimentos = get_estabelecimentos()    
    return render_template("estabelecimentos.html", estabelecimentos=lista_estabelecimentos, total_items=len(lista_estabelecimentos), cidades=get_cidades())

# Rota para receber os dados do formulário e cadastrar estabelecimentos no banco de dados
@app.route('/estabelecimentos/novo', methods=['POST'])
def cadastrar_estabelecimento_route():
    if request.method == "POST":
        cadastrar_estabelecimento(request.form['nome'], request.form['endereco'], request.form['cidade'], request.form['cep'])    
    return redirect(url_for('listar_estabelecimentos'))

# Rota para editar estabelecimentos no banco de dados
@app.route('/estabelecimentos/<int:id>/editar', methods=['GET', 'POST'])
def editar_estabelecimento_route(id):
    if request.method == 'GET':
        # Busca o estabelecimento com o id informado no banco de dados
        estabelecimento = get_estabelecimento_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': estabelecimento['ID'],
            'nome': estabelecimento['NOME'],
            'endereco': estabelecimento['ENDERECO'],
            'cidade': estabelecimento['ID_CIDADE'],
            'cep': estabelecimento['CEP'],
        }
        # Renderiza o template de edição de estabelecimento com os dados da subcategoria encontrada
        return render_template('estabelecimentos.html', item_edit=item_data, cidades=get_cidades())
    elif request.method == 'POST':
        editar_estabelecimento(id, request.form['nome_edit'], request.form['endereco_edit'], request.form['cidade_edit'], request.form['cep_edit'])
        return redirect(url_for('listar_estabelecimentos'))
    
# Rota para excluir subcategorias no banco de dados
@app.route('/estabelecimentos/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_estabelecimento_route(id):
    excluir_estabelecimento(id)    
    return redirect(url_for('listar_estabelecimentos'))

# Rota para tela de formas de pagamento
@app.route("/formasdepagamento")
def listar_formasdepagamento():
    lista_formasdepagamento = get_formasdepagamento()    
    return render_template("formasdepagamento.html", formasdepagamento=lista_formasdepagamento, total_items=len(lista_formasdepagamento))

# Rota para receber os dados do formulário e cadastrar formas de pagamento no banco de dados
@app.route('/formasdepagamento/novo', methods=['POST'])
def cadastrar_formadepagamento_route():
    if request.method == "POST":
        cadastrar_formadepagamento(request.form['descricao'])    
    return redirect(url_for('listar_formasdepagamento'))

# Rota para editar formas de pagamento no banco de dados
@app.route('/formasdepagamento/<int:id>/editar', methods=['GET', 'POST'])
def editar_formadepagamento_route(id):
    if request.method == 'GET':
        # Busca a forma de pagamento com o id informado no banco de dados
        formadepagamento = get_formadepagamento_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': formadepagamento['ID'],
            'descricao': formadepagamento['DESCRICAO']
        }
        # Renderiza o template de edição de forma de pagamento com os dados da subcategoria encontrada
        return render_template('formasdepagamento.html', item_edit=item_data)
    elif request.method == 'POST':
        editar_formadepagamento(id, request.form['descricao_edit'])
        return redirect(url_for('listar_formasdepagamento'))
    
# Rota para excluir subcategorias no banco de dados
@app.route('/formasdepagamento/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_formadepagamento_route(id):
    excluir_formadepagamento(id)    
    return redirect(url_for('listar_formasdepagamento'))

# Rota para tela de listas de compras
@app.route("/listasdecompras")
def listar_listasdecompras():
    lista_listasdecompras = get_listasdecompras()    
    return render_template("listasdecompras.html", listasdecompras=lista_listasdecompras, total_items=len(lista_listasdecompras), estabelecimentos=get_estabelecimentos(), formasdepagamento=get_formasdepagamento())

# Rota para receber os dados do formulário e cadastrar lista de compras no banco de dados
@app.route('/listasdecompras/novo', methods=['POST'])
def cadastrar_listadecompras_route():
    if request.method == "POST":
        cadastrar_listadecompras(request.form['descricao'], request.form['estabelecimento'], request.form['nrocupomfiscal'], request.form['datacompra'], request.form['valorcompra'], request.form['formadepagamento'])    
    return redirect(url_for('listar_listasdecompras'))

# Rota para editar lista de compras no banco de dados
@app.route('/listasdecompras/<int:id>/editar', methods=['GET', 'POST'])
def editar_listadecompras_route(id):
    if request.method == 'GET':
        # Busca o lista de compras com o id informado no banco de dados
        listadecompras = get_listadecompras_por_id(id)
        #Preparar dados do item para exibição
        item_data = {
            'id': listadecompras['ID'],
            'descricao': listadecompras['DESCRICAO'],
            'estabelecimento': listadecompras['ID_Estabelecimento'],
            'nrocupomfiscal': listadecompras['NROCUPOMFISCAL'],
            'datacompra': listadecompras['DATACOMPRA'],
            'valorcompra': listadecompras['VALORCOMPRA'],
        }

        itenslistadecompras = get_itenslistadecompras_por_id_listadecompras(id)
        # Renderiza o template de edição de lista de compras com os dados da subcategoria encontrada
        return render_template('listasdecompras.html', item_edit=item_data, itenslistadecompras=itenslistadecompras , estabelecimentos=get_estabelecimentos(), formasdepagamento=get_formasdepagamento())
    elif request.method == 'POST':
        editar_listadecompras(id, request.form['descricao_edit'], request.form['estabelecimento_edit'], 
                              request.form['nrocupomfiscal_edit'], request.form['datacompra_edit'], 
                              request.form['valorcompra_edit'], request.form['formadepagamento_edit'])
        return redirect(url_for('listar_listasdecompras'))
    
# Rota para excluir lista de compras no banco de dados
@app.route('/listasdecompras/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_listadecompras_route(id):
    excluir_listadecompras(id)    
    return redirect(url_for('listar_listasdecompras'))

@app.route('/products')
def get_products():
    search = request.args.get('search')
    products = get_produtositens()
    
    # Filtragem de produtos de acordo com o termo de busca
    if search:
        filtered_products = [product for product in products if search.lower() in product['DESCRICAO'].lower()]
        return jsonify(filtered_products)
    else:
        return jsonify(products)
    
@app.route('/itenslistadecompras/<int:id_lista>', methods=['GET', 'POST'])
def itens_listadecompras(id_lista):
    if request.method == 'GET':
        itenslistadecompras = get_itenslistadecompras_por_id_listadecompras(id_lista)
        # Código para processar a página "itenslistadecompras.html" com o ID da lista
        return render_template('itenslistadecompras.html', id_lista=id_lista, itenslistadecompras=itenslistadecompras, total_items=len(itenslistadecompras))
    elif request.method == 'POST':
        cadastrar_itenslistadecompras(id_lista,request.form['id_produto'],request.form['quantidade'],request.form['valorproduto'])
    return redirect(url_for('itens_listadecompras', id_lista=id_lista))

# Rota para editar itens da lista de compras no banco de dados
@app.route('/itenslistadecompras/<int:id_lista>/<int:id_produto>/editar', methods=['GET', 'POST'])
def editar_itemlistadecompras_route(id_lista, id_produto):
    if request.method == 'GET':
        # Busca o lista de compras com o id informado no banco de dados
        itemlistadecompras = get_itemlistadecompras_por_ids(id_lista, id_produto)
        #Preparar dados do item para exibição
        item_data = {
            'id_listadecompras': itemlistadecompras['ID_LISTA'],
            'id_produto': itemlistadecompras['ID_PRODUTO'],
            'quantidade': itemlistadecompras['QUANTIDADE'],
            'valor': itemlistadecompras['VALORPRODUTO']
        }

        itenslistadecompras = get_itenslistadecompras_por_id_listadecompras(id_lista)

        # Renderiza o template de edição de lista de compras com os dados da subcategoria encontrada
        return render_template('itenslistadecompras.html', item_edit=item_data, itenslistadecompras=itenslistadecompras)
    elif request.method == 'POST':
        editar_itemlistadecompras(id_lista, request.form['id_produto_edit'], request.form['quantidade_edit'], request.form['valor_edit'])
        return redirect(url_for('itens_listadecompras'))
        
if __name__ == '__main__':
    app.run(debug=True) 