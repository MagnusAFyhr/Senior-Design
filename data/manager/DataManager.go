package manager

type DataManager interface {
	New() error
	ConnectToDatabase() error

	Publish() error
	AddSocket() error
}
