CREATE TABLE FactTable (
    ID_Fact INT PRIMARY KEY,
    ID_Proveedor INT,
    ID_Producto INT,
    ID_Precio INT,
    ID_Boleta INT,
    Cantidad INT,
    PrecioUnitario DECIMAL(10,2),
    PrecioTotalFactura DECIMAL(10,2),
    FechaID INT
);

CREATE TABLE DimProveedores (
    ID_Proveedor INT PRIMARY KEY,
    Proveedor VARCHAR(255),
    Contacto_Comercial VARCHAR(255),
    Email VARCHAR(255),
    Telefono VARCHAR(20)
);

CREATE TABLE DimProductos (
    ID_Producto INT PRIMARY KEY,
    Categoria VARCHAR(255),
    Subcategoria VARCHAR(255),
    Nombre VARCHAR(255)
);

CREATE TABLE DimPrecios (
    ID_Precio INT PRIMARY KEY,
    Precio DECIMAL(10,2),
    Anio INT,
    Mes INT
);

CREATE TABLE DimBoletas (
    ID_Boleta INT PRIMARY KEY,
    Productos VARCHAR(255), -- Puedes ajustar esto según la estructura real
    PrecioTotal DECIMAL(10,2),
    Anio INT,
    Mes INT,
    Dia INT
);

CREATE TABLE DimFechas (
    ID_Fecha INT PRIMARY KEY,
    Anio INT,
    Mes INT,
    Dia INT
);
