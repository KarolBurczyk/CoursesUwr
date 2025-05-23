using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace UserRegistryApp
{
    public class User
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public DateTime DateOfBirth { get; set; }

        public override string ToString() => Name;
    }

    public class CategorySelectedNotification
    {
        public string CategoryName { get; }
        public CategorySelectedNotification(string categoryName) => CategoryName = categoryName;
    }

    public class UserProfileSelectedNotification
    {
        public User User { get; }
        public UserProfileSelectedNotification(User user) => User = user;
    }

    public class UserAddedNotification
    {
        public string CategoryName { get; }
        public User User { get; }
        public UserAddedNotification(string categoryName, User user)
        {
            CategoryName = categoryName;
            User = user;
        }
    }

    public class UserUpdatedNotification
    {
        public string CategoryName { get; }
        public User User { get; }
        public UserUpdatedNotification(string categoryName, User user)
        {
            CategoryName = categoryName;
            User = user;
        }
    }

    public interface ISubscriber<T>
    {
        void Handle(T notification);
    }

    public interface IEventAggregator
    {
        void AddSubscriber<T>(ISubscriber<T> Subscriber);
        void RemoveSubscriber<T>(ISubscriber<T> Subscriber);
        void Publish<T>(T Event);
    }

    public class EventAggregator : IEventAggregator
    {
        private readonly Dictionary<Type, List<object>> _subscribers = new();

        public void AddSubscriber<T>(ISubscriber<T> subscriber)
        {
            var type = typeof(T);
            if (!_subscribers.ContainsKey(type))
                _subscribers[type] = new List<object>();

            _subscribers[type].Add(subscriber);
        }
        public void RemoveSubscriber<T>(ISubscriber<T> subscriber)
        {
            var type = typeof(T);
            if (_subscribers.ContainsKey(type))
                _subscribers[type].Remove(subscriber);
        }

        public void Publish<T>(T notification)
        {
            if (_subscribers.TryGetValue(typeof(T), out var list))
            {
                foreach (var subscriber in list)
                    ((ISubscriber<T>)subscriber).Handle(notification);
            }
        }
    }

    public class UserForm : Form
    {
        public User User { get; private set; }
        private TextBox _txtName, _txtAddress;
        private DateTimePicker _dobPicker;
        private Button _btnOK;

        public UserForm(User user = null)
        {
            Text = user == null ? "Dodaj u¿ytkownika" : "Edytuj u¿ytkownika";
            Size = new Size(300, 250);
            FormBorderStyle = FormBorderStyle.FixedDialog;
            StartPosition = FormStartPosition.CenterParent;

            _txtName = new TextBox { Top = 20, Left = 20, Width = 240, PlaceholderText = "Imiê" };
            _txtAddress = new TextBox { Top = 60, Left = 20, Width = 240, PlaceholderText = "Adres" };
            _dobPicker = new DateTimePicker { Top = 100, Left = 20, Width = 240 };

            _btnOK = new Button { Text = "OK", Top = 150, Left = 20 };
            _btnOK.Click += (s, e) =>
            {
                User = new User
                {
                    Name = _txtName.Text,
                    Address = _txtAddress.Text,
                    DateOfBirth = _dobPicker.Value
                };
                DialogResult = DialogResult.OK;
            };

            Controls.AddRange(new Control[] { _txtName, _txtAddress, _dobPicker, _btnOK });

            if (user != null)
            {
                _txtName.Text = user.Name;
                _txtAddress.Text = user.Address;
                _dobPicker.Value = user.DateOfBirth;
            }
        }
    }

    public class MainForm : Form,
        ISubscriber<CategorySelectedNotification>,
        ISubscriber<UserProfileSelectedNotification>,
        ISubscriber<UserAddedNotification>,
        ISubscriber<UserUpdatedNotification>
    {
        private readonly EventAggregator _aggregator;
        private readonly TreeView _tree;
        private readonly ListView _listView;
        private readonly Label _details;
        private readonly Button _btnAdd, _btnEdit;
        private readonly Dictionary<string, List<User>> _categoryUsers = new();

        private string _currentCategory;
        private User _currentUser;

        public MainForm()
        {
            Text = "Rejestr u¿ytkowników";
            Size = new Size(920, 500);

            _aggregator = new EventAggregator();
            _aggregator.AddSubscriber<CategorySelectedNotification>(this);
            _aggregator.AddSubscriber<UserProfileSelectedNotification>(this);
            _aggregator.AddSubscriber<UserAddedNotification>(this);
            _aggregator.AddSubscriber<UserUpdatedNotification>(this);

            _tree = new TreeView { Dock = DockStyle.Left, Width = 200 };
            _listView = new ListView
            {
                Dock = DockStyle.Top,
                Height = 200,
                View = View.Details,
                FullRowSelect = true
            };
            _listView.Columns.Add("Imiê", 150);
            _listView.Columns.Add("Adres", 200);
            _listView.Columns.Add("Data urodzenia", 120);
            _listView.Click += ListView_Click;

            _details = new Label { Dock = DockStyle.Fill, TextAlign = ContentAlignment.TopLeft };

            _btnAdd = new Button { Text = "Dodaj", Dock = DockStyle.Bottom, Height = 40 };
            _btnAdd.Click += (s, e) => ShowAddDialog();

            _btnEdit = new Button { Text = "Zmieñ", Dock = DockStyle.Bottom, Height = 40 };
            _btnEdit.Click += (s, e) => ShowEditDialog();

            var rightPanel = new Panel { Dock = DockStyle.Fill };
            rightPanel.Controls.Add(_details);
            rightPanel.Controls.Add(_listView);
            rightPanel.Controls.Add(_btnEdit);
            rightPanel.Controls.Add(_btnAdd);

            Controls.Add(_tree);
            Controls.Add(rightPanel);

            _tree.AfterSelect += Tree_AfterSelect;

            PopulateTree();
        }

        private void PopulateTree()
        {
            void AddCategory(TreeNode parent, string categoryName, List<User> users)
            {
                var node = new TreeNode(categoryName) { Tag = categoryName };
                _categoryUsers[categoryName] = users;
                foreach (var user in users)
                {
                    var userNode = new TreeNode(user.Name) { Tag = user };
                    node.Nodes.Add(userNode);
                }
                parent.Nodes.Add(node);
            }

            var students = new TreeNode("Studenci");
            AddCategory(students, "Informatyka", new()
            {
                new User { Name = "Jan Kowalski", Address = "ul. Dêbowa 51, Warszawa", DateOfBirth = new DateTime(1998, 5, 10) },
                new User { Name = "Ewa Nowak", Address = "ul. D³uga 122, Kraków", DateOfBirth = new DateTime(2000, 8, 22) }
            });
            AddCategory(students, "Matematyka", new()
            {
                new User { Name = "Anna Zieliñska", Address = "ul. Lipowa 5, Warszawa", DateOfBirth = new DateTime(1999, 5, 18) }
            });

            var lecturers = new TreeNode("Wyk³adowcy");
            AddCategory(lecturers, "Wydzia³ Informatyki", new()
            {
                new User { Name = "prof. Adam Nowak", Address = "ul. D³uga 12, Kraków", DateOfBirth = new DateTime(1975, 3, 11) }
            });

            _tree.Nodes.Add(students);
            _tree.Nodes.Add(lecturers);
            _tree.ExpandAll();
        }

        private void Tree_AfterSelect(object sender, TreeViewEventArgs e)
        {
            if (e.Node?.Tag is string category)
                _aggregator.Publish(new CategorySelectedNotification(category));
            else if (e.Node?.Tag is User user)
                _aggregator.Publish(new UserProfileSelectedNotification(user));
        }

        private void ListView_Click(object sender, EventArgs e)
        {
            if (_listView.SelectedItems.Count > 0)
            {
                var user = (User)_listView.SelectedItems[0].Tag;
                _aggregator.Publish(new UserProfileSelectedNotification(user));
            }
        }

        private void ShowAddDialog()
        {
            if (string.IsNullOrEmpty(_currentCategory)) return;

            var dialog = new UserForm();
            if (dialog.ShowDialog() == DialogResult.OK)
                _aggregator.Publish(new UserAddedNotification(_currentCategory, dialog.User));
        }

        private void ShowEditDialog()
        {
            if (_currentUser == null) return;

            var dialog = new UserForm(_currentUser);
            if (dialog.ShowDialog() == DialogResult.OK)
                _aggregator.Publish(new UserUpdatedNotification(_currentCategory, dialog.User));
        }

        public void Handle(CategorySelectedNotification notification)
        {
            _currentCategory = notification.CategoryName;
            _currentUser = null;
            _listView.Items.Clear();
            _details.Text = $"Wybrana kategoria: {notification.CategoryName}";

            if (_categoryUsers.TryGetValue(notification.CategoryName, out var users))
            {
                foreach (var user in users)
                {
                    var item = new ListViewItem(user.Name);
                    item.SubItems.Add(user.Address);
                    item.SubItems.Add(user.DateOfBirth.ToString("dd.MM.yyyy"));
                    item.Tag = user;
                    _listView.Items.Add(item);
                }
            }
        }

        public void Handle(UserProfileSelectedNotification notification)
        {
            _currentUser = notification.User;
            _details.Text =
                $"Szczegó³y:\n" +
                $"Imiê i nazwisko: {_currentUser.Name}\n" +
                $"Adres: {_currentUser.Address}\n" +
                $"Data urodzenia: {_currentUser.DateOfBirth:dd.MM.yyyy}";
        }

        public void Handle(UserAddedNotification notification)
        {
            if (!_categoryUsers.ContainsKey(notification.CategoryName))
                _categoryUsers[notification.CategoryName] = new List<User>();

            _categoryUsers[notification.CategoryName].Add(notification.User);

            if (_currentCategory == notification.CategoryName)
                _aggregator.Publish(new CategorySelectedNotification(notification.CategoryName));

            foreach (TreeNode node in _tree.Nodes)
                foreach (TreeNode cat in node.Nodes)
                    if ((string)cat.Tag == notification.CategoryName)
                    {
                        cat.Nodes.Add(new TreeNode(notification.User.Name) { Tag = notification.User });
                        cat.Expand();
                        return;
                    }
        }

        public void Handle(UserUpdatedNotification notification)
        {
            _currentUser.Name = notification.User.Name;
            _currentUser.Address = notification.User.Address;
            _currentUser.DateOfBirth = notification.User.DateOfBirth;
            _aggregator.Publish(new UserProfileSelectedNotification(_currentUser));

            foreach (TreeNode node in _tree.Nodes)
                foreach (TreeNode cat in node.Nodes)
                    if ((string)cat.Tag == notification.CategoryName)
                        foreach (TreeNode userNode in cat.Nodes)
                            if (userNode.Tag == _currentUser)
                                userNode.Text = _currentUser.Name;
        }
    }

    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
