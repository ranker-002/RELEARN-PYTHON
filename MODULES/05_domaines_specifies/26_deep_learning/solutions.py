# =============================================================================
# CHAPITRE 26: DEEP LEARNING - SOLUTIONS
# =============================================================================

# =============================================================================
# EXERCICE 26.1 - PREMIERS TENSEURS
# =============================================================================
def exercice_26_1():
    import torch

    # Tenseur de zéros
    zeros = torch.zeros(3, 3)
    
    # Tenseur de uns
    ones = torch.ones(2, 4)
    
    # Tenseur aléatoire
    random_tensor = torch.rand(2, 3)
    
    # Tenseur avec valeurs spécifiques
    tensor = torch.tensor([1, 2, 3, 4, 5])
    
    print("Tenseur de zéros:")
    print(zeros)
    print("\nTenseur de uns:")
    print(ones)
    print("\nTenseur aléatoire:")
    print(random_tensor)
    print("\nTenseur personnalisé:")
    print(tensor)


# =============================================================================
# EXERCICE 26.2 - OPÉRATIONS SUR TENSEURS
# =============================================================================
def exercice_26_2():
    import torch

    a = torch.tensor([[1, 2], [3, 4]])
    b = torch.tensor([[5, 6], [7, 8]])

    # Addition
    print("Addition:")
    print(a + b)
    print(torch.add(a, b))

    # Multiplication matricielle
    print("\nMultiplication matricielle:")
    print(torch.mm(a, b))
    print(a @ b)

    # Transposition
    print("\nTransposition:")
    print(a.t())

    # Reduction
    print("\nSomme:", a.sum().item())
    print("Moyenne:", a.float().mean().item())


# =============================================================================
# EXERCICE 26.3 - AUTOGRAD
# =============================================================================
def exercice_26_3():
    import torch

    x = torch.tensor(3.0, requires_grad=True)
    y = x ** 2
    y.backward()

    print(f"x = {x.item()}")
    print(f"y = x² = {y.item()}")
    print(f"dy/dx = {x.grad.item()}")


# =============================================================================
# EXERCICE 26.4 - RÉGRESSION LINÉAIRE PYTORCH
# =============================================================================
def exercice_26_4():
    import torch
    import torch.nn as nn
    import torch.optim as optim

    X = torch.tensor([[1], [2], [3], [4], [5]], dtype=torch.float32)
    y = torch.tensor([[2], [4], [6], [8], [10]], dtype=torch.float32)

    model = nn.Linear(1, 1)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(1000):
        predictions = model(X)
        loss = criterion(predictions, y)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Poids: {model.weight.item():.4f}")
    print(f"Biais: {model.bias.item():.4f}")
    print(f"Loss finale: {loss.item():.6f}")


# =============================================================================
# EXERCICE 26.5 - RÉSEAU DE NEURONES SIMPLE
# =============================================================================
def exercice_26_5():
    import torch
    import torch.nn as nn

    class Reseau(nn.Module):
        def __init__(self, input_size, hidden1, hidden2, output_size):
            super().__init__()
            self.fc1 = nn.Linear(input_size, hidden1)
            self.fc2 = nn.Linear(hidden1, hidden2)
            self.fc3 = nn.Linear(hidden2, output_size)
        
        def forward(self, x):
            x = torch.relu(self.fc1(x))
            x = torch.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    model = Reseau(4, 8, 4, 1)
    print(model)

    # Test forward pass
    x = torch.randn(1, 4)
    print(f"Input: {x}")
    print(f"Output: {model(x)}")


# =============================================================================
# EXERCICE 26.6 - FONCTIONS D'ACTIVATION
# =============================================================================
def exercice_26_6():
    import torch
    import torch.nn as nn

    x = torch.linspace(-5, 5, 100)

    activations = {
        'ReLU': torch.relu(x),
        'Sigmoid': torch.sigmoid(x),
        'Tanh': torch.tanh(x),
        'LeakyReLU': torch.nn.functional.leaky_relu(x),
    }

    for name, act in activations.items():
        print(f"{name}: min={act.min():.4f}, max={act.max():.4f}")


# =============================================================================
# EXERCICE 26.7 - CNN SIMPLE
# =============================================================================
def exercice_26_7():
    import torch
    import torch.nn as nn

    class CNN(nn.Module):
        def __init__(self, num_classes=10):
            super().__init__()
            self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
            self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
            self.pool = nn.MaxPool2d(2, 2)
            self.fc1 = nn.Linear(32 * 8 * 8, 128)
            self.fc2 = nn.Linear(128, num_classes)
        
        def forward(self, x):
            x = self.pool(torch.relu(self.conv1(x)))
            x = self.pool(torch.relu(self.conv2(x)))
            x = x.view(-1, 32 * 8 * 8)
            x = torch.relu(self.fc1(x))
            x = self.fc2(x)
            return x

    model = CNN()
    print(f"Nombre de paramètres: {sum(p.numel() for p in model.parameters()):,}")

    # Test
    x = torch.randn(1, 3, 32, 32)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {model(x).shape}")


# =============================================================================
# EXERCICE 26.8 - DATA LOADING
# =============================================================================
def exercice_26_8():
    import torch
    from torch.utils.data import Dataset, DataLoader

    class MonDataset(Dataset):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __len__(self):
            return len(self.x)
        
        def __getitem__(self, idx):
            return self.x[idx], self.y[idx]

    x = torch.randn(100, 4)
    y = torch.randint(0, 5, (100,))

    dataset = MonDataset(x, y)
    loader = DataLoader(dataset, batch_size=10, shuffle=True)

    print(f"Nombre d'échantillons: {len(dataset)}")
    print(f"Nombre de batches: {len(loader)}")

    for batch_x, batch_y in loader:
        print(f"Batch X shape: {batch_x.shape}")
        print(f"Batch Y shape: {batch_y.shape}")
        break


# =============================================================================
# EXERCICE 26.9 - TRANSFER LEARNING
# =============================================================================
def exercice_26_9():
    import torch
    import torchvision.models as models
    import torch.nn as nn

    # Charger ResNet18 pré-entraîné
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)

    # Geler les couches
    for param in model.parameters():
        param.requires_grad = False

    # Remplacer la dernière couche
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, 10)  # 10 classes

    # Compter paramètres entraînables
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    print(f"Paramètres entraînables: {trainable:,} / {total:,}")


# =============================================================================
# EXERCICE 26.10 - LSTM
# =============================================================================
def exercice_26_10():
    import torch
    import torch.nn as nn

    class LSTMModel(nn.Module):
        def __init__(self, input_size, hidden_size, num_layers, output_size):
            super().__init__()
            self.hidden_size = hidden_size
            self.num_layers = num_layers
            self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
            self.fc = nn.Linear(hidden_size, output_size)
        
        def forward(self, x):
            h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
            c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
            out, _ = self.lstm(x, (h0, c0))
            out = self.fc(out[:, -1, :])
            return out

    model = LSTMModel(input_size=1, hidden_size=64, num_layers=2, output_size=1)
    x = torch.randn(32, 10, 1)  # (batch, seq_len, features)
    out = model(x)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {out.shape}")


# =============================================================================
# EXERCICE 26.11 - SAVE/LOAD MODEL
# =============================================================================
def exercice_26_11():
    import torch
    import torch.nn as nn

    class Model(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc = nn.Linear(4, 1)
        
        def forward(self, x):
            return self.fc(x)

    model = Model()

    # Sauvegarder
    torch.save({
        'model_state_dict': model.state_dict(),
        'fc_weight': model.fc.weight.item(),
        'fc_bias': model.fc.bias.item(),
    }, 'model.pth')

    # Charger
    checkpoint = torch.load('model.pth')
    model.load_state_dict(checkpoint['model_state_dict'])
    
    print(f"Poids chargé: {checkpoint['fc_weight']}")
    print("Modèle sauvegardé et chargé avec succès!")


# =============================================================================
# EXERCICE 26.12 - GPU UTILISATION
# =============================================================================
def exercice_26_12():
    import torch
    import torch.nn as nn

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Device: {device}")

    model = nn.Linear(4, 1).to(device)
    x = torch.randn(2, 4).to(device)
    
    out = model(x)
    print(f"Output: {out}")
    print(f"Output device: {out.device}")


# =============================================================================
# EXERCICE 26.13 - DROPOUT ET BATCHNORM
# =============================================================================
def exercice_26_13():
    import torch
    import torch.nn as nn

    class ReseauAvance(nn.Module):
        def __init__(self):
            super().__init__()
            self.block = nn.Sequential(
                nn.Linear(10, 64),
                nn.BatchNorm1d(64),
                nn.ReLU(),
                nn.Dropout(0.3),
                nn.Linear(64, 32),
                nn.BatchNorm1d(32),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(32, 1)
            )
        
        def forward(self, x):
            return self.block(x)

    model = ReseauAvance()
    print(f"Nombre de couches BatchNorm: {sum(1 for m in model.modules() if isinstance(m, nn.BatchNorm1d))}")
    print(f"Nombre de couches Dropout: {sum(1 for m in model.modules() if isinstance(m, nn.Dropout))}")


# =============================================================================
# EXERCICE 26.14 - CUSTOM LOSS
# =============================================================================
def exercice_26_14():
    import torch
    import torch.nn as nn

    class CustomLoss(nn.Module):
        def __init__(self, alpha=0.5):
            super().__init__()
            self.alpha = alpha
        
        def forward(self, predictions, targets):
            mse = nn.MSELoss()(predictions, targets)
            mae = nn.L1Loss()(predictions, targets)
            return self.alpha * mse + (1 - self.alpha) * mae

    criterion = CustomLoss(alpha=0.7)
    pred = torch.tensor([1.0, 2.0, 3.0])
    target = torch.tensor([1.1, 2.1, 2.9])
    
    loss = criterion(pred, target)
    print(f"Custom Loss: {loss.item():.4f}")


# =============================================================================
# EXERCICE 26.15 - PROJET COMPLET
# =============================================================================
def exercice_26_15():
    import torch
    import torch.nn as nn
    import torch.optim as optim
    from torch.utils.data import DataLoader, TensorDataset

    # Générer données
    X = torch.randn(1000, 4)
    y = (X[:, 0] + 0.5 * X[:, 1] - X[:, 2] > 0).float().view(-1, 1)

    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=64, shuffle=True)

    # Modèle
    class Classifier(nn.Module):
        def __init__(self):
            super().__init__()
            self.layers = nn.Sequential(
                nn.Linear(4, 32),
                nn.ReLU(),
                nn.BatchNorm1d(32),
                nn.Dropout(0.3),
                nn.Linear(32, 16),
                nn.ReLU(),
                nn.Linear(16, 1),
                nn.Sigmoid()
            )
        
        def forward(self, x):
            return self.layers(x)

    model = Classifier()
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Entraînement
    for epoch in range(20):
        model.train()
        total_loss = 0
        correct = 0
        total = 0
        
        for x_batch, y_batch in loader:
            optimizer.zero_grad()
            outputs = model(x_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            predicted = (outputs > 0.5).float()
            total += y_batch.size(0)
            correct += (predicted == y_batch).sum().item()
        
        accuracy = 100 * correct / total
        print(f'Epoch {epoch+1}: Loss={total_loss/len(loader):.4f}, Accuracy={accuracy:.1f}%')

    # Évaluation finale
    model.eval()
    with torch.no_grad():
        predictions = model(X)
        final_acc = ((predictions > 0.5).float() == y).float().mean().item()
    print(f'\nAccuracy finale: {final_acc*100:.1f}%')
