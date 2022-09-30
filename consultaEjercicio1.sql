SELECT LibroID as "Identificador del libro" , Titulo as "Título del libro",  Nombre, Apellidos
FROM Libros L
JOIN Autores A on L.AutorID = A.AutorID
WHERE Costo > 12
LIMIT 20;
