package socket

type DataSocket interface {
	New() error
	Connect() error

	Push() error
	// Recover() error

	// ...
}
