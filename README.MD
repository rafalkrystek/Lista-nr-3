# Automatyzacja Testów API z użyciem curl

## Opis

Ten skrypt automatyzuje testowanie endpointów API za pomocą `curl`. Wysyła żądania HTTP GET do wybranych publicznych endpointów API, sprawdza status odpowiedzi HTTP, parsuje odpowiedzi JSON i weryfikuje obecność kluczowych elementów w odpowiedziach. Wyniki testów są wyświetlane w czytelny sposób.

## Testowane API

- [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

## Endpointy i Wymagane Klucze

1. `/posts/1`: `userId`, `id`, `title`, `body`
2. `/comments/1`: `postId`, `id`, `name`, `email`, `body`
3. `/users/1`: `id`, `name`, `username`, `email`

## Jak Uruchomić Skrypt

1. Upewnij się, że Python jest zainstalowany.
2. Zapisz skrypt jako `api_test.py`.
3. Uruchom skrypt w terminalu:
   ```bash
   python api_test.py

