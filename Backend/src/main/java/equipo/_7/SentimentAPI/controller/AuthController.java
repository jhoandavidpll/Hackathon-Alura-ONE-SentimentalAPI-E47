package equipo._7.SentimentAPI.controller;

import equipo._7.SentimentAPI.domain.user.DataAuth;
import equipo._7.SentimentAPI.domain.user.DataRegister;
import equipo._7.SentimentAPI.domain.user.User;
import equipo._7.SentimentAPI.domain.user.UserRepository;
import equipo._7.SentimentAPI.infra.security.DataTokenJWT;
import equipo._7.SentimentAPI.infra.security.TokenService;
import equipo._7.SentimentAPI.infra.security.exceptions.ValidacionDeNegocioException; // Importamos la nueva excepción
import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.ResponseEntity; // Agregado para devolver ResponseEntity

import java.util.Objects;

@RestController
@RequestMapping
public class AuthController {

    @Autowired
    private TokenService tokenService;
    @Autowired
    private AuthenticationManager manager;
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private PasswordEncoder passwordEncoder;

    @PostMapping("/login")
    public ResponseEntity<DataTokenJWT> login(@RequestBody @Valid DataAuth data) {
        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
        var auth = manager.authenticate(authToken);
        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
        return ResponseEntity.ok(new DataTokenJWT(tokenJwt));
    }

    @Transactional
    @PostMapping("/register")
    public ResponseEntity<DataTokenJWT> register(@RequestBody @Valid DataRegister data) {
    
        if (!Objects.equals(data.password(), data.passwordConfirmation())) {
            throw new ValidacionDeNegocioException("Las contraseñas no coinciden");
        }
        
        var user = new User(data.email(), encodePassword(data.password()));
        userRepository.save(user);
        
        var authToken = new UsernamePasswordAuthenticationToken(data.email(), data.password());
        var auth = manager.authenticate(authToken);
        var tokenJwt = tokenService.generateToken((User) auth.getPrincipal());
        
        return ResponseEntity.ok(new DataTokenJWT(tokenJwt));
    }

    private String encodePassword(String password) {
        return passwordEncoder.encode(password);
    }
}