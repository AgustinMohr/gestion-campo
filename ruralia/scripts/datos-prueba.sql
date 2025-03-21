-- Insertar datos en campo_producto
INSERT INTO campo_producto (nombre, descripcion, cantidad, unidad_medida)
VALUES
    ('Fertilizante A', 'Fertilizante para mejorar el rendimiento de los cultivos', 100.00, 'kg'),
    ('Agroquímico B', 'Pesticida para controlar plagas', 200.00, 'l'),
    ('Semilla C', 'Semilla para cultivo de maíz', 500.00, 'unidades'),
    ('Herbicida D', 'Herbicida para controlar maleza', 150.00, 'l'),
    ('Fertilizante E', 'Fertilizante para frutas', 120.00, 'kg');

-- Insertar datos en campo_lote
INSERT INTO campo_lote (nombre, superficie)
VALUES
    ('Lote 1', 1500.00),
    ('Lote 2', 2000.00),
    ('Lote 3', 1800.00),
    ('Lote 4', 2500.00),
    ('Lote 5', 1700.00);

-- Insertar datos en campo_movimientostock
-- El tipo de movimiento puede ser 'entrada' o 'salida', dependiendo de si el stock aumenta o disminuye.
INSERT INTO campo_movimientostock (cantidad, tipo_movimiento, fecha, producto_id)
VALUES
    (50.00, 'entrada', '2025-03-01 10:00:00', 1),  -- Producto 1 (Fertilizante A)
    (30.00, 'salida', '2025-03-02 12:00:00', 1),  -- Producto 1 (Fertilizante A)
    (100.00, 'entrada', '2025-03-03 09:00:00', 2),  -- Producto 2 (Agroquímico B)
    (20.00, 'salida', '2025-03-04 14:00:00', 3),  -- Producto 3 (Semilla C)
    (50.00, 'entrada', '2025-03-05 16:00:00', 4),  -- Producto 4 (Herbicida D)
    (10.00, 'salida', '2025-03-06 18:00:00', 5);  -- Producto 5 (Fertilizante E)

-- Insertar datos en campo_aplicacion
-- Para este ejemplo, asignamos los productos y lotes que ya existen. La cantidad_usada se refiere a la cantidad de producto aplicado.
INSERT INTO campo_aplicacion (cantidad_usada, fecha, lote_id, producto_id)
VALUES
    (25.00, '2025-03-07', 1, 1),  -- Aplicación de Fertilizante A en Lote 1
    (40.00, '2025-03-08', 2, 2),  -- Aplicación de Agroquímico B en Lote 2
    (60.00, '2025-03-09', 3, 3),  -- Aplicación de Semilla C en Lote 3
    (30.00, '2025-03-10', 4, 4),  -- Aplicación de Herbicida D en Lote 4
    (50.00, '2025-03-11', 5, 5);  -- Aplicación de Fertilizante E en Lote 5

