SELECT Nombre, Descripcion as "Descripción del estado actual de la aplicación", FechaCambio as "Fecha del último cambio de estado"
FROM Aplicacion A JOIN HistoricoEstadosAplicacion H on A.IdAplicacion=H.IdAplicacion
JOIN EstadosAplicacion E on  E.IdEstado=H.IdEstado;