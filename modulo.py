import sqlite3
from time import sleep

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)
meses = {
    "01": "Enero",
    "02": "Febrero",
    "03": "Marzo",
    "04": "Abril",
    "05": "Mayo",
    "06": "Junio",
    "07": "Julio",
    "08": "Agosto",
    "09": "Septiembre",
    "10": "Octubre",
    "11": "Noviembre",
    "12": "Diciembre",
}

ruta = 'C:\\Desarrollo\\TallerMecanico\\base.db'


# *******************************************************************************************************
# **************************************** Funciones de Clientes ****************************************
# *******************************************************************************************************

def actualizar_cliente(campo, campo_valor, identificador):
    """Actualiza los renglones de la tabla clientes"""
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('UPDATE clientes SET {} = {} WHERE clientes_id = {}'.format(campo, "'" + campo_valor + "'", identificador))
    conexion.commit()
    conexion.close() 


def actualizar_vector_cliente(cliente, telefono, direccion, email, identificador):
    actualizar_cliente("cliente", cliente, identificador)
    actualizar_cliente("cliente_telefono", telefono, identificador)
    actualizar_cliente("cliente_direccion", direccion, identificador)
    actualizar_cliente("cliente_correo", email, identificador)


def buscar_cliente(identificador):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM clientes')
    resultado = cursor.fetchall()
    conexion.close()
    lista = []
    for elemento in resultado:
        if elemento[1] == identificador:
            lista.append(elemento)
    return lista


def consultar_cliente(identificador):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM clientes WHERE clientes_id = {}'.format(identificador))
    cliente = cursor.fetchone()
    conexion.close()
    return cliente


def consultar_clientes():
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conexion.close()
    return clientes


def ingresar_cliente(cliente, telefono, direccion, email):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    datos    = [cliente, telefono, direccion, email]
    cursor.execute('INSERT INTO clientes VALUES (null,?,?,?,?)', datos)
    conexion.commit()    
    conexion.close()
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    datos    = [cliente, telefono, direccion, email]
    cursor.execute('SELECT * FROM clientes WHERE cliente = ? AND cliente_telefono = ? AND cliente_direccion = ? AND cliente_correo = ?', datos)
    consulta = cursor.fetchone()
    conexion.close()
    return consulta


def procesar_texto_clientes(texto):
    if texto.isdigit():
        consulta = consultar_cliente(texto)
        if consulta == None:
            return 0
        else:
            return consulta            
    else:
        consulta = buscar_cliente(texto)
        if consulta == []:
            return 0
        else:
            return consulta[0]


# *******************************************************************************************************
# **************************************** Funciones de Trabajos ****************************************
# *******************************************************************************************************

def actualizar_trabajo(campo, campo_valor, identificador):
    """Actualiza los renglones de la tabla trabajos"""
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('UPDATE trabajos SET {} = {} WHERE trabajos_id = {}'.format(campo, "'" + campo_valor + "'", identificador))
    conexion.commit()
    conexion.close() 


def actualizar_vector_trabajo(trabajo, descripcion, auto, precio, inicio, final, estatus, prioridad, identificador):
    actualizar_trabajo("trabajos", trabajo, identificador)
    actualizar_trabajo("trabajos_descripcion", descripcion, identificador)
    actualizar_trabajo("trabajos_auto", auto, identificador)
    actualizar_trabajo("trabajos_precio", precio, identificador)
    actualizar_trabajo("trabajos_inicio", inicio, identificador)
    actualizar_trabajo("trabajos_final", final, identificador)
    actualizar_trabajo("trabajos_estatus", estatus, identificador)
    actualizar_trabajo("trabajos_prioridad", prioridad, identificador)


def buscar_trabajo(identificador):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM trabajos')
    resultado = cursor.fetchall()
    conexion.close()
    lista = []
    for elemento in resultado:
        if str(elemento[0]) == identificador:
            lista.append(elemento)
    return lista


def consultar_trabajo(identificador):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM trabajos WHERE trabajos_id = {}'.format(identificador))
    trabajo = cursor.fetchone()
    conexion.close()
    return trabajo


def consultar_trabajos():
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM trabajos')
    trabajos = cursor.fetchall()
    conexion.close()
    return trabajos


def contar_trabajos():
    lista      = consultar_trabajos()
    agendados  = 0
    terminados = 0
    proceso    = 0
    for elemento in lista:
        if elemento[7] == "Agendado":
            agendados += 1
        elif elemento[7] == "Terminado":
            terminados += 1
        elif elemento[7] == "En Proceso":
            proceso += 1
    return [agendados, terminados, proceso]


def ingresar_trabajo(trabajo, descripcion, auto, precio, inicio, final, estatus, prioridad, cliente):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    datos    = [trabajo, descripcion, auto, precio, inicio, final, estatus, prioridad, cliente]
    cursor.execute('INSERT INTO trabajos VALUES (null,?,?,?,?,?,?,?,?,?)', datos)
    conexion.commit()
    conexion.close()
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    datos    = [trabajo, descripcion, auto, precio, inicio, final, estatus, prioridad, cliente]
    cursor.execute('SELECT * FROM trabajos WHERE trabajos = ? AND trabajos_descripcion = ? AND trabajos_auto = ? AND trabajos_precio = ? AND trabajos_inicio = ? AND trabajos_final = ? AND trabajos_estatus = ? AND trabajos_prioridad = ? AND trabajos_clientes = ?', datos)
    consulta = cursor.fetchone()
    conexion.close()
    return consulta


# ***********************************************************************************************************
# **************************************** Funciones de Herramientas ****************************************
# ***********************************************************************************************************

def actualizar_herramienta(campo, campo_valor, identificador):
    """Actualiza los renglones de la tabla herramientas"""
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('UPDATE herramientas SET {} = {} WHERE herramientas_id = {}'.format(campo, "'" + campo_valor + "'", identificador))
    conexion.commit()
    conexion.close() 


def actualizar_vector_herramienta(herramienta, detalle, unidades, estado, identificador):
    actualizar_herramienta("herramientas", herramienta, identificador)
    actualizar_herramienta("herramientas_detalle", detalle, identificador)
    actualizar_herramienta("herramientas_unidades", unidades, identificador)
    actualizar_herramienta("herramientas_estado", estado, identificador)


def buscar_herramienta(identificador):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM herramientas')
    resultado = cursor.fetchall()
    conexion.close()
    lista = []
    for elemento in resultado:
        if str(elemento[0]) == identificador:
            lista.append(elemento)
    return lista


def consultar_herramienta(identificador):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM herramientas WHERE herramientas_id = {}'.format(identificador))
    cliente = cursor.fetchone()
    conexion.close()
    return cliente


def consultar_herramientas():
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM herramientas')
    clientes = cursor.fetchall()
    conexion.close()
    return clientes


def ingresar_herramienta(herramienta, detalle, unidades, estado):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    datos    = [herramienta, detalle, unidades, estado]
    cursor.execute('INSERT INTO herramientas VALUES (null,?,?,?,?)', datos)
    conexion.commit()    
    conexion.close()


# *********************************************************************************************************
# **************************************** Funciones de Inventario ****************************************
# *********************************************************************************************************

def actualizar_inventario(campo, campo_valor, identificador):
    """Actualiza los renglones de la tabla herramientas"""
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('UPDATE inventario SET {} = {} WHERE inventario_id = {}'.format(campo, "'" + campo_valor + "'", identificador))
    conexion.commit()
    conexion.close() 


def actualizar_vector_inventario(inventario, detalle, unidades, estado, identificador):
    actualizar_inventario("inventario", inventario, identificador)
    actualizar_inventario("inventario_detalle", detalle, identificador)
    actualizar_inventario("inventario_unidades", unidades, identificador)
    actualizar_inventario("inventario_estado", estado, identificador)


def buscar_inventario(identificador):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM inventario')
    resultado = cursor.fetchall()
    conexion.close()
    lista = []
    for elemento in resultado:
        if str(elemento[0]) == identificador:
            lista.append(elemento)
    return lista


def consultar_inventario(identificador):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM inventario WHERE inventario_id = {}'.format(identificador))
    cliente = cursor.fetchone()
    conexion.close()
    return cliente


def consultar_inventarios():
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('SELECT * FROM inventario')
    clientes = cursor.fetchall()
    conexion.close()
    return clientes


def ingresar_inventario(refaccion, detalle, unidades, estado):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    datos    = [refaccion, detalle, unidades, estado]
    cursor.execute('INSERT INTO inventario VALUES (null,?,?,?,?)', datos)
    conexion.commit()    
    conexion.close()


# *****************************************************************************************************
# **************************************** Funciones Generales ****************************************
# *****************************************************************************************************

def eliminar_dato(tabla, identificador):
    conexion = sqlite3.connect(ruta)
    cursor   = conexion.cursor()
    cursor.execute('DELETE FROM {} WHERE {}_id = {}'.format(tabla, tabla, identificador))
    conexion.commit()    
    conexion.close()


def procesar_fecha(entrada, caracter):
    vector = entrada.split(caracter)
    if len(vector[0]) > 2:
        return "{} de {} de {}".format(vector[2], meses[vector[1]], vector[0])
    else:
        return "{} de {} de {}".format(vector[0], meses[vector[1]], vector[2])


def recuperar_fecha(entrada, caracter):
    vector = entrada.split(caracter)
    llave = ""
    for elemento in meses:
        if meses[elemento] == vector[1]:
            llave = elemento
    if len(vector[0]) == 1:
        return "{}-{}-{}".format("0" + vector[0], llave,vector[2]) 
    else:
        return "{}-{}-{}".format(vector[0], llave,vector[2])

LICENCIA = """
\t\t                                 Apache License
\t\t                           Version 2.0, January 2004
\t\t                        http://www.apache.org/licenses/
\t\t
\t\t   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
\t\t
\t\t   1. Definitions.
\t\t
\t\t      "License" shall mean the terms and conditions for use, reproduction,
\t\t      and distribution as defined by Sections 1 through 9 of this document.
\t\t
\t\t      "Licensor" shall mean the copyright owner or entity authorized by
\t\t      the copyright owner that is granting the License.
\t\t
\t\t      "Legal Entity" shall mean the union of the acting entity and all
\t\t      other entities that control, are controlled by, or are under common
\t\t      control with that entity. For the purposes of this definition,
\t\t      "control" means (i) the power, direct or indirect, to cause the
\t\t      direction or management of such entity, whether by contract or
\t\t      otherwise, or (ii) ownership of fifty percent (50%) or more of the
\t\t      outstanding shares, or (iii) beneficial ownership of such entity.
\t\t
\t\t      "You" (or "Your") shall mean an individual or Legal Entity
\t\t      exercising permissions granted by this License.
\t\t
\t\t      "Source" form shall mean the preferred form for making modifications,
\t\t      including but not limited to software source code, documentation
\t\t      source, and configuration files.
\t\t
\t\t      "Object" form shall mean any form resulting from mechanical
\t\t      transformation or translation of a Source form, including but
\t\t      not limited to compiled object code, generated documentation,
\t\t      and conversions to other media types.
\t\t
\t\t      "Work" shall mean the work of authorship, whether in Source or
\t\t      Object form, made available under the License, as indicated by a
\t\t      copyright notice that is included in or attached to the work
\t\t      (an example is provided in the Appendix below).
\t\t
\t\t      "Derivative Works" shall mean any work, whether in Source or Object
\t\t      form, that is based on (or derived from) the Work and for which the
\t\t      editorial revisions, annotations, elaborations, or other modifications
\t\t      represent, as a whole, an original work of authorship. For the purposes
\t\t      of this License, Derivative Works shall not include works that remain
\t\t      separable from, or merely link (or bind by name) to the interfaces of,
\t\t      the Work and Derivative Works thereof.
\t\t
\t\t      "Contribution" shall mean any work of authorship, including
\t\t      the original version of the Work and any modifications or additions
\t\t      to that Work or Derivative Works thereof, that is intentionally
\t\t      submitted to Licensor for inclusion in the Work by the copyright owner
\t\t      or by an individual or Legal Entity authorized to submit on behalf of
\t\t      the copyright owner. For the purposes of this definition, "submitted"
\t\t      means any form of electronic, verbal, or written communication sent
\t\t      to the Licensor or its representatives, including but not limited to
\t\t      communication on electronic mailing lists, source code control systems,
\t\t      and issue tracking systems that are managed by, or on behalf of, the
\t\t      Licensor for the purpose of discussing and improving the Work, but
\t\t      excluding communication that is conspicuously marked or otherwise
\t\t      designated in writing by the copyright owner as "Not a Contribution."
\t\t
\t\t      "Contributor" shall mean Licensor and any individual or Legal Entity
\t\t      on behalf of whom a Contribution has been received by Licensor and
\t\t      subsequently incorporated within the Work.
\t\t
\t\t   2. Grant of Copyright License. Subject to the terms and conditions of
\t\t      this License, each Contributor hereby grants to You a perpetual,
\t\t      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
\t\t      copyright license to reproduce, prepare Derivative Works of,
\t\t      publicly display, publicly perform, sublicense, and distribute the
\t\t      Work and such Derivative Works in Source or Object form.
\t\t
\t\t   3. Grant of Patent License. Subject to the terms and conditions of
\t\t      this License, each Contributor hereby grants to You a perpetual,
\t\t      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
\t\t      (except as stated in this section) patent license to make, have made,
\t\t      use, offer to sell, sell, import, and otherwise transfer the Work,
\t\t      where such license applies only to those patent claims licensable
\t\t      by such Contributor that are necessarily infringed by their
\t\t      Contribution(s) alone or by combination of their Contribution(s)
\t\t      with the Work to which such Contribution(s) was submitted. If You
\t\t      institute patent litigation against any entity (including a
\t\t      cross-claim or counterclaim in a lawsuit) alleging that the Work
\t\t      or a Contribution incorporated within the Work constitutes direct
\t\t      or contributory patent infringement, then any patent licenses
\t\t      granted to You under this License for that Work shall terminate
\t\t      as of the date such litigation is filed.
\t\t
\t\t   4. Redistribution. You may reproduce and distribute copies of the
\t\t      Work or Derivative Works thereof in any medium, with or without
\t\t      modifications, and in Source or Object form, provided that You
\t\t      meet the following conditions:
\t\t
\t\t      (a) You must give any other recipients of the Work or
\t\t          Derivative Works a copy of this License; and
\t\t
\t\t      (b) You must cause any modified files to carry prominent notices
\t\t          stating that You changed the files; and
\t\t
\t\t      (c) You must retain, in the Source form of any Derivative Works
\t\t          that You distribute, all copyright, patent, trademark, and
\t\t          attribution notices from the Source form of the Work,
\t\t          excluding those notices that do not pertain to any part of
\t\t          the Derivative Works; and
\t\t
\t\t      (d) If the Work includes a "NOTICE" text file as part of its
\t\t          distribution, then any Derivative Works that You distribute must
\t\t          include a readable copy of the attribution notices contained
\t\t          within such NOTICE file, excluding those notices that do not
\t\t          pertain to any part of the Derivative Works, in at least one
\t\t          of the following places: within a NOTICE text file distributed
\t\t          as part of the Derivative Works; within the Source form or
\t\t          documentation, if provided along with the Derivative Works; or,
\t\t          within a display generated by the Derivative Works, if and
\t\t          wherever such third-party notices normally appear. The contents
\t\t          of the NOTICE file are for informational purposes only and
\t\t          do not modify the License. You may add Your own attribution
\t\t          notices within Derivative Works that You distribute, alongside
\t\t          or as an addendum to the NOTICE text from the Work, provided
\t\t          that such additional attribution notices cannot be construed
\t\t          as modifying the License.
\t\t
\t\t      You may add Your own copyright statement to Your modifications and
\t\t      may provide additional or different license terms and conditions
\t\t      for use, reproduction, or distribution of Your modifications, or
\t\t      for any such Derivative Works as a whole, provided Your use,
\t\t      reproduction, and distribution of the Work otherwise complies with
\t\t      the conditions stated in this License.
\t\t
\t\t   5. Submission of Contributions. Unless You explicitly state otherwise,
\t\t      any Contribution intentionally submitted for inclusion in the Work
\t\t      by You to the Licensor shall be under the terms and conditions of
\t\t      this License, without any additional terms or conditions.
\t\t      Notwithstanding the above, nothing herein shall supersede or modify
\t\t      the terms of any separate license agreement you may have executed
\t\t      with Licensor regarding such Contributions.
\t\t
\t\t   6. Trademarks. This License does not grant permission to use the trade
\t\t      names, trademarks, service marks, or product names of the Licensor,
\t\t      except as required for reasonable and customary use in describing the
\t\t      origin of the Work and reproducing the content of the NOTICE file.
\t\t
\t\t   7. Disclaimer of Warranty. Unless required by applicable law or
\t\t      agreed to in writing, Licensor provides the Work (and each
\t\t      Contributor provides its Contributions) on an "AS IS" BASIS,
\t\t      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
\t\t      implied, including, without limitation, any warranties or conditions
\t\t      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
\t\t      PARTICULAR PURPOSE. You are solely responsible for determining the
\t\t      appropriateness of using or redistributing the Work and assume any
\t\t      risks associated with Your exercise of permissions under this License.
\t\t
\t\t   8. Limitation of Liability. In no event and under no legal theory,
\t\t      whether in tort (including negligence), contract, or otherwise,
\t\t      unless required by applicable law (such as deliberate and grossly
\t\t      negligent acts) or agreed to in writing, shall any Contributor be
\t\t      liable to You for damages, including any direct, indirect, special,
\t\t      incidental, or consequential damages of any character arising as a
\t\t      result of this License or out of the use or inability to use the
\t\t      Work (including but not limited to damages for loss of goodwill,
\t\t      work stoppage, computer failure or malfunction, or any and all
\t\t      other commercial damages or losses), even if such Contributor
\t\t      has been advised of the possibility of such damages.
\t\t
\t\t   9. Accepting Warranty or Additional Liability. While redistributing
\t\t      the Work or Derivative Works thereof, You may choose to offer,
\t\t      and charge a fee for, acceptance of support, warranty, indemnity,
\t\t      or other liability obligations and/or rights consistent with this
\t\t      License. However, in accepting such obligations, You may act only
\t\t      on Your own behalf and on Your sole responsibility, not on behalf
\t\t      of any other Contributor, and only if You agree to indemnify,
\t\t      defend, and hold each Contributor harmless for any liability
\t\t      incurred by, or claims asserted against, such Contributor by reason
\t\t      of your accepting any such warranty or additional liability.
\t\t
\t\t   END OF TERMS AND CONDITIONS
\t\t
\t\t   APPENDIX: How to apply the Apache License to your work.
\t\t
\t\t      To apply the Apache License to your work, attach the following
\t\t      boilerplate notice, with the fields enclosed by brackets "[]"
\t\t      replaced with your own identifying information. (Don't include
\t\t      the brackets!)  The text should be enclosed in the appropriate
\t\t      comment syntax for the file format. We also recommend that a
\t\t      file or class name and description of purpose be included on the
\t\t      same "printed page" as the copyright notice for easier
\t\t      identification within third-party archives.
\t\t
\t\t   Copyright [yyyy] [name of copyright owner]
\t\t
\t\t   Licensed under the Apache License, Version 2.0 (the "License");
\t\t   you may not use this file except in compliance with the License.
\t\t   You may obtain a copy of the License at
\t\t
\t\t       http://www.apache.org/licenses/LICENSE-2.0
\t\t
\t\t   Unless required by applicable law or agreed to in writing, software
\t\t   distributed under the License is distributed on an "AS IS" BASIS,
\t\t   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
\t\t   See the License for the specific language governing permissions and
\t\t   limitations under the License.
\t\t
"""