
Querys={

"producao":"""
            SELECT 
                tb1.id_prod,tb1.initial_date,tb1.final_date,SUM(tb2.quantidade)
            FROM
                producao tb1 INNER JOIN materiais_producao tb2 on tb1.id_prod = tb2.id_prod
            GROUP BY
                tb1.id_prod 
            ORDER BY tb1.id_prod DESC

""",

"Producao_Dt":"""

            SELECT
                tb1.id_prod,tb1.initial_date,tb1.final_date,SUM(tb2.quantidade)
            FROM
                producao tb1 INNER JOIN materiais_producao tb2 on tb1.id_prod = tb2.id_prod 
            WHERE 
                tb1.initial_date >= %s AND tb1.final_date <= %s
            GROUP BY 
                tb1.id_prod  
            ORDER BY tb1.id_prod DESC

"""
}