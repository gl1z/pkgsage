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
('Humanizer', 'Humanizer', 'Humanizer', 7),

-- Microsoft.Extensions.DependencyInjection
('IServiceCollection', 'Microsoft.Extensions.DependencyInjection', 'Microsoft.Extensions.DependencyInjection', 10),
('ServiceCollection', 'Microsoft.Extensions.DependencyInjection', 'Microsoft.Extensions.DependencyInjection', 9),
('IServiceProvider', 'Microsoft.Extensions.DependencyInjection', 'Microsoft.Extensions.DependencyInjection', 9),
('ServiceDescriptor', 'Microsoft.Extensions.DependencyInjection', 'Microsoft.Extensions.DependencyInjection', 7),

-- Microsoft.Extensions.Configuration
('IConfiguration', 'Microsoft.Extensions.Configuration', 'Microsoft.Extensions.Configuration', 10),
('ConfigurationBuilder', 'Microsoft.Extensions.Configuration', 'Microsoft.Extensions.Configuration', 9),
('IConfigurationSection', 'Microsoft.Extensions.Configuration', 'Microsoft.Extensions.Configuration', 8),

-- Microsoft.Extensions.Logging
('ILogger', 'Microsoft.Extensions.Logging', 'Microsoft.Extensions.Logging', 10),
('ILoggerFactory', 'Microsoft.Extensions.Logging', 'Microsoft.Extensions.Logging', 9),
('LoggerFactory', 'Microsoft.Extensions.Logging', 'Microsoft.Extensions.Logging', 8),
('ILoggerProvider', 'Microsoft.Extensions.Logging', 'Microsoft.Extensions.Logging', 7),

-- Microsoft.Extensions.Caching.Memory
('IMemoryCache', 'Microsoft.Extensions.Caching.Memory', 'Microsoft.Extensions.Caching.Memory', 9),
('MemoryCache', 'Microsoft.Extensions.Caching.Memory', 'Microsoft.Extensions.Caching.Memory', 8),
('MemoryCacheEntryOptions', 'Microsoft.Extensions.Caching.Memory', 'Microsoft.Extensions.Caching.Memory', 7),

-- EF Core extras
('ModelBuilder', 'Microsoft.EntityFrameworkCore', 'Microsoft.EntityFrameworkCore', 9),
('DbContextOptions', 'Microsoft.EntityFrameworkCore', 'Microsoft.EntityFrameworkCore', 9),
('DbContextOptionsBuilder', 'Microsoft.EntityFrameworkCore', 'Microsoft.EntityFrameworkCore', 8),
('IEntityTypeConfiguration', 'Microsoft.EntityFrameworkCore', 'Microsoft.EntityFrameworkCore', 8),
('EntityTypeBuilder', 'Microsoft.EntityFrameworkCore', 'Microsoft.EntityFrameworkCore', 7),
('MigrationBuilder', 'Microsoft.EntityFrameworkCore.Migrations', 'Microsoft.EntityFrameworkCore', 7),

-- MediatR extras
('IRequestHandler', 'MediatR', 'MediatR', 9),
('INotification', 'MediatR', 'MediatR', 8),
('INotificationHandler', 'MediatR', 'MediatR', 8),
('ISender', 'MediatR', 'MediatR', 7),

-- FluentAssertions
('AndConstraint', 'FluentAssertions', 'FluentAssertions', 7),
('AssertionScope', 'FluentAssertions', 'FluentAssertions', 7),
('ExecutionTimeAssertions', 'FluentAssertions', 'FluentAssertions', 6),

-- AutoFixture
('Fixture', 'AutoFixture', 'AutoFixture', 9),
('IFixture', 'AutoFixture', 'AutoFixture', 8),
('ICustomization', 'AutoFixture', 'AutoFixture', 7),

-- Hangfire
('BackgroundJob', 'Hangfire', 'Hangfire', 9),
('RecurringJob', 'Hangfire', 'Hangfire', 9),
('IBackgroundJobClient', 'Hangfire', 'Hangfire', 8),
('IRecurringJobManager', 'Hangfire', 'Hangfire', 7),

-- Refit
('IRestService', 'Refit', 'Refit', 8),
('RefitSettings', 'Refit', 'Refit', 7),
('ApiException', 'Refit', 'Refit', 7),

-- xUnit
('Fact', 'Xunit', 'xunit', 9),
('Theory', 'Xunit', 'xunit', 9),
('InlineData', 'Xunit', 'xunit', 8),
('ITestOutputHelper', 'Xunit.Abstractions', 'xunit', 7),

-- NUnit
('TestFixture', 'NUnit.Framework', 'NUnit', 9),
('SetUp', 'NUnit.Framework', 'NUnit', 8),
('TearDown', 'NUnit.Framework', 'NUnit', 8),
('Assert', 'NUnit.Framework', 'NUnit', 7),

-- Serilog extras
('LoggerConfiguration', 'Serilog', 'Serilog', 9),
('LogEventLevel', 'Serilog.Events', 'Serilog', 8),
('LogEvent', 'Serilog.Events', 'Serilog', 7),

-- AutoMapper extras
('Profile', 'AutoMapper', 'AutoMapper', 9),
('IMappingExpression', 'AutoMapper', 'AutoMapper', 7);