CREATE TABLE IF NOT EXISTS symbols (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    namespace TEXT,
    package TEXT NOT NULL,
    confidence INTEGER DEFAULT 1
);

CREATE INDEX IF NOT EXISTS idx_symbol ON symbols(symbol);

INSERT INTO symbols (symbol, namespace, package, confidence) VALUES
('JsonConvert', 'Newtonsoft.Json', 'Newtonsoft.Json', 10),
('JObject', 'Newtonsoft.Json', 'Newtonsoft.Json', 10),
('JArray', 'Newtonsoft.Json', 'Newtonsoft.Json', 9),
('DbContext', 'Microsoft.EntityFrameworkCore', 'Microsoft.EntityFrameworkCore', 10),
('DbSet', 'Microsoft.EntityFrameworkCore', 'Microsoft.EntityFrameworkCore', 10),
('IMapper', 'AutoMapper', 'AutoMapper', 9),
('MapperConfiguration', 'AutoMapper', 'AutoMapper', 8),
('AbstractValidator', 'FluentValidation', 'FluentValidation', 9),
('ValidationResult', 'FluentValidation', 'FluentValidation', 8),
('IMediator', 'MediatR', 'MediatR', 9),
('IRequest', 'MediatR', 'MediatR', 8),
('RestClient', 'RestSharp', 'RestSharp', 9),
('RestRequest', 'RestSharp', 'RestSharp', 8),
('ConnectionMultiplexer', 'StackExchange.Redis', 'StackExchange.Redis', 9),
('MongoClient', 'MongoDB.Driver', 'MongoDB.Driver', 9),
('IMongoCollection', 'MongoDB.Driver', 'MongoDB.Driver', 8),
('CsvReader', 'CsvHelper', 'CsvHelper', 9),
('CsvWriter', 'CsvHelper', 'CsvHelper', 8),
('Faker', 'Bogus', 'Bogus', 8),
('Policy', 'Polly', 'Polly', 9),
('AsyncPolicy', 'Polly', 'Polly', 8),
('SqlMapper', 'Dapper', 'Dapper', 9),
('Serilog', 'Serilog', 'Serilog', 9),
('Log', 'Serilog', 'Serilog', 8),
('WebApplication', 'Microsoft.AspNetCore', 'Microsoft.AspNetCore.App', 7),
('HttpClient', 'System.Net.Http', 'System.Net.Http', 7),
('JsonSerializer', 'System.Text.Json', 'System.Text.Json', 8),
('Mock', 'Moq', 'Moq', 9),
('It', 'Moq', 'Moq', 8),
('Humanizer', 'Humanizer', 'Humanizer', 7);
