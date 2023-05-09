from flask_mysqldb import MySQL

mysql = MySQL()

# função para buscar perfis no banco
def get_perfis():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT P.ID, P.DESCRICAO FROM perfil P')
        perfis = cursor.fetchall()
    return perfis

# função para buscar um perfil específico
def get_perfil_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT P.ID, P.DESCRICAO FROM perfil P WHERE ID=%s', (id,))
        perfil = cursor.fetchone()        
    return perfil

# função para cadastrar perfis no banco de dados
def cadastrar_perfil(descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO Perfil (Descricao) VALUES (%s)', (descricao,))
        mysql.connection.commit()

# Rota para editar perfis no banco de dados
def editar_perfil(id, descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE Perfil SET Descricao=%s WHERE ID=%s', (descricao, id))
        mysql.connection.commit()

# Rota para excluir perfis no banco de dados
def excluir_perfil(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM Perfil WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar usuários no banco
def get_usuarios():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT U.ID, U.NOME, U.EMAIL, P.DESCRICAO AS PERFIL FROM USUARIO U INNER JOIN PERFIL P ON U.ID_Perfil = P.ID')
        usuarios = cursor.fetchall()
    return usuarios

# função para buscar um usuario específico
def get_usuario_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT U.ID, U.NOME, U.APELIDO, U.EMAIL, U.DATANASCIMENTO, ID_PERFIL, SENHA FROM usuario U WHERE ID=%s', (id,))
        usuario = cursor.fetchone()   
    return usuario

# função para cadastrar usuários no banco de dados
def cadastrar_usuario(nome, apelido, email, data_nascimento, id_perfil, senha):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO Usuario (Nome, Apelido, Email, DataNascimento, ID_Perfil, Senha) VALUES (%s, %s, %s, %s, %s, %s)', (nome, apelido, email, data_nascimento, id_perfil, senha))
        mysql.connection.commit()

# Rota para editar usuários no banco de dados
def editar_usuario(id, nome, apelido, email, data_nascimento, id_perfil, senha):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE Usuario SET Nome=%s, Apelido=%s, email=%s, data_nascimento=%s, id_perfil=%s, senha=%s WHERE ID=%s', (nome, apelido, email, data_nascimento, id_perfil, senha, id))
        mysql.connection.commit()

# Rota para excluir usuários no banco de dados
def excluir_usuario(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM Usuario WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar categorias no banco
def get_categorias():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT C.ID, C.DESCRICAO FROM categoria C')
        categorias = cursor.fetchall()
    return categorias

# função para buscar uma categoria específica
def get_categoria_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT C.ID, C.DESCRICAO FROM categoria C WHERE ID=%s', (id,))
        categoria = cursor.fetchone()        
    return categoria

# função para cadastrar categorias no banco de dados
def cadastrar_categoria(descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO Categoria (Descricao) VALUES (%s)', (descricao,))
        mysql.connection.commit()

# Rota para editar categorias no banco de dados
def editar_categoria(id, descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE Categoria SET Descricao=%s WHERE ID=%s', (descricao, id))
        mysql.connection.commit()

# Rota para excluir categorias no banco de dados
def excluir_categoria(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM Categoria WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar subcategorias no banco
def get_subcategorias():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT SC.ID, C.DESCRICAO AS CATEGORIA, SC.DESCRICAO FROM subcategoria SC INNER JOIN categoria C ON SC.ID_Categoria = C.ID')
        subcategorias = cursor.fetchall()
    return subcategorias

# função para buscar uma subcategoria específica
def get_subcategoria_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT SC.ID, SC.ID_Categoria, SC.DESCRICAO FROM subcategoria SC WHERE ID=%s', (id,))
        subcategoria = cursor.fetchone()        
    return subcategoria

# função para buscar uma subcategoria de uma categoriaespecífica
def get_subcategorias_por_categoria(id_categoria):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT SC.ID, SC.ID_Categoria, SC.DESCRICAO FROM subcategoria SC WHERE SC.ID_Categoria=%s ORDER BY SC.DESCRICAO', (id_categoria,))
        subcategorias = cursor.fetchall()        
    return subcategorias

# função para cadastrar subcategorias no banco de dados
def cadastrar_subcategoria(id_categoria, descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO subcategoria (ID_Categoria, Descricao) VALUES (%s,%s)', (id_categoria,descricao))
        mysql.connection.commit()

# Rota para editar subcategorias no banco de dados
def editar_subcategoria(id, id_categoria, descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE subcategoria SET ID_Categoria=%s, Descricao=%s WHERE ID=%s', (id_categoria, descricao, id))
        mysql.connection.commit()

# Rota para excluir subcategorias no banco de dados
def excluir_subcategoria(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM subcategoria WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar unidades de medida no banco
def get_unidadesdemedida():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT UM.ID, UM.DESCRICAO FROM unidadedemedida UM')
        unidadesdemedida = cursor.fetchall()
    return unidadesdemedida

# função para buscar uma unidade de medida específica
def get_unidadedemedida_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT UM.ID, UM.DESCRICAO FROM unidadedemedida UM WHERE ID=%s', (id,))
        unidadedemedida = cursor.fetchone()        
    return unidadedemedida

# função para cadastrar unidades de medida no banco de dados
def cadastrar_unidadedemedida(descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO unidadedemedida (Descricao) VALUES (%s)', (descricao,))
        mysql.connection.commit()

# Rota para editar unidades de medida no banco de dados
def editar_unidadedemedida(id, descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE unidadedemedida SET Descricao=%s WHERE ID=%s', (descricao, id))
        mysql.connection.commit()

# Rota para excluir unidades de medida no banco de dados
def excluir_unidadedemedida(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM unidadedemedida WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar locais da casa de medida no banco
def get_locaisdacasa():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT LC.ID, LC.DESCRICAO FROM localdacasa LC')
        locaisdacasa = cursor.fetchall()
    return locaisdacasa

# função para buscar um local da casa específica
def get_localdacasa_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT LC.ID, LC.DESCRICAO FROM localdacasa LC WHERE ID=%s', (id,))
        localdacasa = cursor.fetchone()        
    return localdacasa

# função para cadastrar locais da casa no banco de dados
def cadastrar_localdacasa(descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO localdacasa (Descricao) VALUES (%s)', (descricao,))
        mysql.connection.commit()

# Rota para editar locais da casa no banco de dados
def editar_localdacasa(id, descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE localdacasa SET Descricao=%s WHERE ID=%s', (descricao, id))
        mysql.connection.commit()

# Rota para excluir locais da casa no banco de dados
def excluir_localdacasa(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM localdacasa WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar produtos no banco
def get_produtos():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT P.ID, P.DESCRICAO, C.DESCRICAO AS CATEGORIA, SC.DESCRICAO AS SUBCATEGORIA, '
               'UM.DESCRICAO AS UNIDADEDEMEDIDA, LC.DESCRICAO AS LOCALDACASA, P.DATAATUALIZACAO, '
               'P.DATAVENCIMENTO, P.QUANTIDADEESTOQUE, '
               'P.QUANTIDADEMINIMA, P.PERECIVEL '
               'FROM produto P '
               'INNER JOIN categoria C ON P.ID_Categoria = C.ID '
               'INNER JOIN subcategoria SC ON P.ID_Subcategoria = SC.ID '
               'INNER JOIN unidadedemedida UM ON P.ID_UnidadedeMedida = UM.ID '
               'INNER JOIN localdacasa LC ON P.ID_LocaldaCasa = LC.ID ORDER BY P.DESCRICAO')
        produtos = cursor.fetchall()
    return produtos

# função para buscar um produto específico
def get_produto_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT P.ID, P.DESCRICAO, P.ID_CATEGORIA, P.ID_SUBCATEGORIA, '
                       'P.ID_UNIDADEDEMEDIDA, P.ID_LOCALDACASA, P.DATAATUALIZACAO, '
                       'P.DATAVENCIMENTO, P.QUANTIDADEESTOQUE, P.QUANTIDADEMINIMA, '
                       'P.PERECIVEL FROM produto P WHERE ID=%s', (id,))
        produto = cursor.fetchone()        
    return produto

# função para cadastrar produtos no banco de dados
def cadastrar_produto(descricao, id_categoria, id_subcategoria, id_unidadedemedida, id_localdacasa, datavencimento, quantidadeestoque, quantidademinima, perecivel):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO Produto (Descricao, ID_Categoria, ID_SubCategoria, ID_UnidadedeMedida, '
                       'id_localdacasa, dataatualizacao, datavencimento, quantidadeestoque, quantidademinima, '
                       'perecivel) VALUES (%s,%s,%s,%s,%s,SYSDATE(),%s,%s,%s,%s)', (descricao, id_categoria, id_subcategoria, id_unidadedemedida, id_localdacasa, datavencimento, quantidadeestoque, quantidademinima, perecivel))
        mysql.connection.commit()

# Rota para editar produtos no banco de dados
def editar_produto(id, descricao, id_categoria, id_subcategoria, id_unidadedemedida, id_localcasa, datavencimento, quantidadeestoque, quantidademinima, perecivel):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE Produto SET Descricao=%s, ID_Categoria=%s, ID_SubCategoria=%s, ID_UnidadedeMedida=%s, '
                       'id_localdacasa=%s, dataatualizacao=SYSDATE(), datavencimento=%s, quantidadeestoque=%s, quantidademinima=%s, '
                       'perecivel=%s WHERE ID=%s', (descricao, id_categoria, id_subcategoria, id_unidadedemedida, id_localcasa, datavencimento, quantidadeestoque, quantidademinima, perecivel, id))
        mysql.connection.commit()

# Rota para excluir produtos no banco de dados
def excluir_produto(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM Produto WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar estabelecimentos no banco
def get_estabelecimentos():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT E.ID, E.NOME, E.ENDERECO, C.NOME AS CIDADE, E.CEP FROM estabelecimento E '
                       'INNER JOIN cidade C ON E.ID_Cidade = C.ID')
        estabelecimentos = cursor.fetchall()
    return estabelecimentos

# função para buscar cidades no banco
def get_cidades():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT C.ID, C.NOME, E.UF FROM cidade C '
                       'INNER JOIN estado E ON C.ID_Estado = E.ID')
        cidades = cursor.fetchall()
    return cidades

# função para buscar um estabelecimento específica
def get_estabelecimento_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT E.ID, E.NOME, E.ENDERECO, E.ID_CIDADE, E.CEP FROM estabelecimento E WHERE ID=%s', (id,))
        estabelecimento = cursor.fetchone()        
    return estabelecimento

# função para cadastrar estabelecimentos no banco de dados
def cadastrar_estabelecimento(nome, endereco, id_cidade, cep):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO estabelecimento (Nome, Endereco, ID_Cidade, CEP) VALUES (%s,%s,%s,%s)', (nome, endereco, id_cidade, cep))
        mysql.connection.commit()

# Rota para editar estabelecimentos no banco de dados
def editar_estabelecimento(id, nome, endereco, id_cidade, cep):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE estabelecimento SET nome=%s, endereco=%s, id_cidade=%s, cep=%s WHERE ID=%s', (nome, endereco, id_cidade, cep, id))
        mysql.connection.commit()

# Rota para excluir estabelecimentos no banco de dados
def excluir_estabelecimento(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM estabelecimento WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar formas de pagamento no banco
def get_formasdepagamento():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT FP.ID, FP.DESCRICAO FROM formadepagamento FP')
        formasdepagamento = cursor.fetchall()
    return formasdepagamento

# função para buscar uma forma de pagamento específica
def get_formadepagamento_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT FP.ID, FP.DESCRICAO FROM formadepagamento FP WHERE ID=%s', (id,))
        formadepagamento = cursor.fetchone()        
    return formadepagamento

# função para cadastrar forma de pagamento no banco de dados
def cadastrar_formadepagamento(descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO formadepagamento (descricao) VALUES (%s)', (descricao,))
        mysql.connection.commit()

# Rota para editar formas de pagamento no banco de dados
def editar_formadepagamento(id, descricao):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE formadepagamento SET descricao=%s WHERE ID=%s', (descricao, id))
        mysql.connection.commit()

# Rota para excluir formas de pagamento no banco de dados
def excluir_formadepagamento(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM formadepagamento WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar listas de compras no banco
def get_listasdecompras():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT LC.ID, LC.DESCRICAO, E.NOME AS ESTABELECIMENTO, LC.DATACOMPRA, LC.VALORCOMPRA FROM listadecompras LC '
                       'INNER JOIN estabelecimento E ON LC.ID_Estabelecimento = E.ID ORDER BY LC.DATACOMPRA DESC')
        listasdecompras = cursor.fetchall()
    return listasdecompras

# função para buscar uma lista de compras específica
def get_listadecompras_por_id(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT LC.ID, LC.DESCRICAO, LC.ID_Estabelecimento, LC.NROCUPOMFISCAL, LC.DATACOMPRA, LC.VALORCOMPRA, LC.ID_FormadePagamento FROM listadecompras LC WHERE ID=%s', (id,))
        listadecompras = cursor.fetchone()        
    return listadecompras

# função para cadastrar lista de compras no banco de dados
def cadastrar_listadecompras(descricao, id_estabelecimento, nrocupomfiscal, datacompra, valorcompra, id_formadepagamento):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO listadecompras (descricao, id_estabelecimento, nrocupomfiscal, datacompra, valorcompra, id_formadepagamento) VALUES (%s,%s,%s,%s,%s,%s)', (descricao, id_estabelecimento, nrocupomfiscal, datacompra, valorcompra, id_formadepagamento))
        mysql.connection.commit()

# Rota para editar lista de compras no banco de dados
def editar_listadecompras(id, descricao, id_estabelecimento, nrocupomfiscal, datacompra, valorcompra, id_formadepagamento):
    with mysql.connection.cursor() as cursor:
        cursor.execute('UPDATE listadecompras SET descricao=%s, id_estabelecimento=%s, nrocupomfiscal=%s, datacompra=%s, valorcompra=%s, id_formadepagamento=%s WHERE ID=%s', (descricao, id_estabelecimento, nrocupomfiscal, datacompra, valorcompra, id_formadepagamento, id))
        mysql.connection.commit()

# Rota para excluir lista de compras no banco de dados
def excluir_listadecompras(id):
    with mysql.connection.cursor() as cursor:
        cursor.execute('DELETE FROM listadecompras WHERE ID = %s', (id,))
        mysql.connection.commit()

# função para buscar itens da lista de compras no banco
def get_itenslistadecompras_por_id_listadecompras(id_listadecompras):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT ILC.ID_ListadeCompras, ILC.ID_Produto, P.DESCRICAO AS PRODUTO, ILC.QUANTIDADE, ILC.VALORPRODUTO '
                       'FROM itenslistadecompras ILC '
                       'INNER JOIN produto P ON ILC.ID_Produto = P.ID '
                       ' WHERE ILC.ID_ListadeCompras = %s ORDER BY P.DESCRICAO DESC', (id_listadecompras,))
        itenslistasdecompras = cursor.fetchall()
    return itenslistasdecompras

# função para cadastrar itens da lista de compras no banco de dados
def cadastrar_itenslistadecompras(id_listadecompras, id_produto, quantidade, valorproduto):
    with mysql.connection.cursor() as cursor:
        cursor.execute('INSERT INTO itenslistadecompras (id_listadecompras, id_produto, quantidade, valorproduto) VALUES (%s,%s,%s,%s)', (id_listadecompras, id_produto, quantidade, valorproduto))
        mysql.connection.commit()

def get_produtositens():
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT DESCRICAO FROM produto')
        produtos = [produto[0] for produto in cursor.fetchall()]
    return produtos

def get_produtos_by_termo(termo):
    with mysql.connection.cursor() as cursor:
        cursor.execute('SELECT ID, DESCRICAO FROM produto WHERE DESCRICAO LIKE %s', ('%' + termo + '%',))
        produtos = cursor.fetchall()
    return produtos